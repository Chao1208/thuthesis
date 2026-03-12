#!/bin/bash

# 安装编译论文所需的 LaTeX 包
echo "正在安装编译所需的 LaTeX 包..."
echo "注意：安装过程中需要输入管理员密码"

export PATH="/Library/TeX/texbin:$PATH"

# 更新 tlmgr
echo "更新 tlmgr..."
sudo tlmgr update --self

# 安装必需的包
echo "安装必需的包..."
sudo tlmgr install \
    ctex \
    latexmk \
    xetex \
    xelatex \
    xeCJK \
    fontspec \
    xunicode \
    xltxtra \
    realscripts \
    metalogo \
    fixltx2e \
    etoolbox \
    xpatch \
    zhnumber \
    zhspacing \
    fandol \
    titletoc \
    notoccite \
    filehook \
    xparse \
    geometry \
    fancyhdr \
    amsmath \
    graphicx \
    subcaption \
    pdfpages \
    enumitem \
    environ \
    footmisc \
    xeCJKfntef \
    array \
    booktabs \
    url \
    natbib

echo ""
echo "✅ 安装完成！现在可以编译论文了"
echo ""
echo "使用方法："
echo "  ./compile.sh my-thesis"
echo "或者"
echo "  make thesis"

