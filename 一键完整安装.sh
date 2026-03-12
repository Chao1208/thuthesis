#!/bin/bash

# ============================================
# 一键安装所有缺失的包并编译
# ============================================

export PATH="/Library/TeX/texbin:$PATH"

echo "============================================"
echo "一键安装所有缺失的 LaTeX 包"
echo "============================================"
echo ""

echo "将要安装以下包："
echo "  LaTeX 包："
echo "    - bibunits (参考文献)"
echo "    - tex-gyre, tex-gyre-math (西文字体)"
echo "    - xits (数学字体)"
echo ""

# 安装所有缺失的包
echo "步骤 1: 安装包..."
sudo tlmgr install bibunits tex-gyre tex-gyre-math xits

echo ""
echo "步骤 2: 更新文件索引..."
sudo mktexlsr

echo ""
echo "步骤 3: 清理旧文件..."
make clean
rm -f my-thesis.*

echo ""
echo "步骤 4: 确保 my-thesis.tex 存在..."
if [ ! -f "my-thesis.tex" ]; then
    cp thuthesis-example.tex my-thesis.tex
    # 修改为使用 fandol 字体
    sed -i.bak 's/\\documentclass\[degree=master\]/\\documentclass[degree=master,fontset=fandol]/' my-thesis.tex
    echo "已创建 my-thesis.tex（使用 fandol 字体）"
fi

echo ""
echo "步骤 5: 编译论文..."
make thesis

echo ""
echo "============================================"
if [ -f "my-thesis.pdf" ]; then
    echo "✅ 编译成功！"
    echo "============================================"
    echo ""
    ls -lh my-thesis.pdf
else
    echo "❌ 编译失败，查看错误信息："
    echo "============================================"
    tail -30 my-thesis.log | grep -i "error\|not found"
fi

