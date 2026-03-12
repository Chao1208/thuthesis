#!/bin/bash

# 快速安装当前缺失的包并编译

export PATH="/Library/TeX/texbin:$PATH"

echo "安装 bibunits..."
sudo tlmgr install bibunits

echo ""
echo "清理并编译..."
make clean
make thesis

echo ""
echo "检查 PDF..."
ls -lh my-thesis.pdf 2>/dev/null && echo "✅ 编译成功！" || echo "❌ 编译失败"

