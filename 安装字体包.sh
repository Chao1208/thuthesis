#!/bin/bash

# 安装编译所需的所有字体包

export PATH="/Library/TeX/texbin:$PATH"

echo "============================================"
echo "安装编译所需的字体包"
echo "============================================"
echo ""

echo "需要安装以下字体包："
echo "  - tex-gyre (TeX Gyre 字体系列)"
echo "  - tex-gyre-math (数学字体)"
echo "  - xits (XITS 数学字体)"
echo ""

sudo tlmgr install tex-gyre tex-gyre-math xits

echo ""
echo "更新文件索引..."
sudo mktexlsr

echo ""
echo "验证安装..."
kpsewhich texgyretermes-regular.otf
kpsewhich xits-math.otf

echo ""
echo "============================================"
echo "✅ 安装完成！"
echo "============================================"
echo ""
echo "现在可以编译："
echo "  make thesis"

