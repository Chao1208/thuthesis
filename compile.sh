#!/bin/bash

# 编译论文脚本（不需要 latexmk）
# 使用方法: ./compile.sh [thesis-file-name]

# 设置 LaTeX 路径
export PATH="/Library/TeX/texbin:$PATH"

# 获取论文文件名（默认为 my-thesis.tex）
THESIS=${1:-my-thesis}
THESIS_FILE="${THESIS}.tex"

# 检查文件是否存在
if [ ! -f "$THESIS_FILE" ]; then
    echo "错误：找不到文件 $THESIS_FILE"
    exit 1
fi

echo "正在编译 $THESIS_FILE..."
echo ""

# 第一次编译
echo "第一次编译 (xelatex)..."
xelatex -interaction=nonstopmode "$THESIS" || exit 1

# 编译参考文献（如果存在 .bib 文件）
if [ -f "ref/refs.bib" ] || [ -f "${THESIS}.bib" ]; then
    echo ""
    echo "编译参考文献 (bibtex)..."
    bibtex "$THESIS" || echo "警告：bibtex 编译失败，继续编译..."
fi

# 第二次编译
echo ""
echo "第二次编译 (xelatex)..."
xelatex -interaction=nonstopmode "$THESIS" || exit 1

# 第三次编译（确保交叉引用正确）
echo ""
echo "第三次编译 (xelatex)..."
xelatex -interaction=nonstopmode "$THESIS" || exit 1

echo ""
echo "✅ 编译完成！输出文件：${THESIS}.pdf"

