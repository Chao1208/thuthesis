# Makefile for ThuThesis

PACKAGE = thuthesis
THESIS  = my-thesis
SPINE   = spine

SOURCES = $(PACKAGE).ins $(PACKAGE).dtx
CLSFILE = dtx-style.sty $(PACKAGE).cls

# Add LaTeX to PATH on macOS if not already present
ifneq ($(OS),Windows_NT)
  ifeq ($(shell uname),Darwin)
    TEXBIN := /Library/TeX/texbin
    ifneq ($(wildcard $(TEXBIN)),)
      PATH := $(TEXBIN):$(PATH)
      export PATH
    endif
  endif
endif

LATEXMK = latexmk
SHELL  := /usr/bin/env bash

# make deletion work on Windows
ifdef SystemRoot
	RM = del /Q
else
	RM = rm -f
endif

.PHONY: all all-dev clean distclean dist thesis viewthesis doc viewdoc cls check save test FORCE_MAKE

thesis: $(THESIS).pdf

all: thesis

all-dev: doc all

cls: $(CLSFILE)

$(CLSFILE): $(SOURCES)
	@if [ -d /Library/TeX/texbin ]; then export PATH="/Library/TeX/texbin:$$PATH"; fi; \
	xetex $(PACKAGE).ins

doc: $(PACKAGE).pdf

$(PACKAGE).pdf: cls FORCE_MAKE
	@if [ -d /Library/TeX/texbin ]; then export PATH="/Library/TeX/texbin:$$PATH"; fi; \
	$(LATEXMK) $(PACKAGE).dtx

$(THESIS).pdf: cls FORCE_MAKE
	@if [ -d /Library/TeX/texbin ]; then export PATH="/Library/TeX/texbin:$$PATH"; fi; \
	$(LATEXMK) $(THESIS)

viewdoc: doc
	$(LATEXMK) -pv $(PACKAGE).dtx

viewthesis: thesis
	$(LATEXMK) -pv $(THESIS)

save:
ifeq ($(target),)
	bash testfiles/save.sh
else
	bash testfiles/save.sh $(target)
endif

test:
ifeq ($(target),)
	l3build check
else
	bash testfiles/test.sh $(target)
endif

clean:
	@if [ -d /Library/TeX/texbin ]; then export PATH="/Library/TeX/texbin:$$PATH"; fi; \
	$(LATEXMK) -c $(PACKAGE).dtx $(THESIS) thuthesis-example
	-@$(RM) -rf *~ main-survey.* main-translation.* _markdown_thuthesis* thuthesis.markdown.*

cleanall: clean
	-@$(RM) $(PACKAGE).pdf $(THESIS).pdf thuthesis-example.pdf

distclean: cleanall
	-@$(RM) $(CLSFILE)
	-@$(RM) -r dist

check: FORCE_MAKE
ifeq ($(version),)
	@echo "Error: version missing: \"make [check|dist] version=X.Y.Z\""; exit 1
else
	@[[ $(shell grep -E -c '$(version) Tsinghua University Thesis Template|\\def\\version\{$(version)\}' thuthesis.dtx) -eq 3 ]] || (echo "bump version with \"l3build tag\" before release"; exit 1)
endif

dist: check all-dev
	# use l3build for CTAN release (zip with .tds.zip)
	l3build ctan --config utils/build-ctan
	# use gulp for GitHub release (zip with generated file)
	python3 utils/create_release.py --version="v$(version)"
