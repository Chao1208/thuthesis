#!/bin/bash

# ============================================
# 一键安装 thuthesis 模板所需的所有 LaTeX 包
# ============================================

# 不设置 set -e，允许部分包安装失败（可能已安装）

echo "============================================"
echo "正在安装 thuthesis 模板所需的所有 LaTeX 包"
echo "============================================"
echo ""

# 设置 LaTeX 路径
export PATH="/Library/TeX/texbin:$PATH"

# 检查 tlmgr 是否可用
if ! command -v tlmgr &> /dev/null; then
    echo "错误：找不到 tlmgr 命令"
    echo "请确保已安装 BasicTeX 或 MacTeX"
    exit 1
fi

echo "步骤 1/3: 更新 tlmgr..."
sudo tlmgr update --self || echo "警告：tlmgr 更新失败，继续..."

echo ""
echo "步骤 2/3: 安装核心中文支持包..."
sudo tlmgr install \
    ctex \
    zhnumber \
    zhspacing \
    fandol \
    fontspec \
    xunicode \
    xltxtra \
    realscripts || echo "警告：部分包安装失败"

echo ""
echo "步骤 3/3: 安装模板所需的所有宏包..."
echo "注意：某些包可能已包含在其他包中，安装时会自动处理"
sudo tlmgr install \
    latexmk \
    xetex \
    iftex \
    kvdefinekeys \
    kvsetkeys \
    kvoptions \
    etoolbox \
    filehook \
    l3packages \
    geometry \
    fancyhdr \
    titlesec \
    notoccite \
    amsmath \
    graphics \
    caption \
    pdfpages \
    enumitem \
    environ \
    footmisc \
    bigfoot \
    perpage \
    tools \
    booktabs \
    url \
    natbib \
    amscls \
    threeparttable \
    multirow \
    algorithms \
    siunitx \
    hyperref \
    metalogo \
    xpatch \
    ulem || echo "警告：部分包安装失败"

echo ""
echo "============================================"
echo "✅ 安装完成！"
echo "============================================"
echo ""
echo "现在可以编译论文了："
echo "  make thesis"
echo "或者"
echo "  ./compile.sh my-thesis"
echo ""

