#!/bin/bash

# ============================================
# 智能安装缺失的 LaTeX 包
# 先检查缺失，再安装
# ============================================

export PATH="/Library/TeX/texbin:$PATH"

echo "============================================"
echo "检查并安装缺失的 LaTeX 包"
echo "============================================"
echo ""

# 检查函数
check_and_install() {
    local package=$1
    local file=$2
    
    if [ -z "$file" ]; then
        # 如果没有指定文件，直接尝试安装包
        echo "安装包: $package"
        sudo tlmgr install "$package" 2>&1 | grep -v "already present" || true
    else
        # 检查文件是否存在
        if ! kpsewhich "$file" > /dev/null 2>&1; then
            echo "缺失: $file (包: $package)"
            sudo tlmgr install "$package" 2>&1 | grep -v "already present" || true
        else
            echo "已存在: $file"
        fi
    fi
}

echo "步骤 1: 安装核心缺失包..."
check_and_install "titlesec" "titletoc.sty"
check_and_install "l3packages" "xparse.sty"
check_and_install "graphics" "graphicx.sty"
check_and_install "amscls" "amsthm.sty"
check_and_install "tools" "longtable.sty"
check_and_install "algorithms" "algorithm.sty"
check_and_install "caption" "subcaption.sty"

echo ""
echo "步骤 2: 安装其他可能缺失的包..."
# 这些包可能已经包含在基础安装中，但确保安装
PACKAGES=(
    "array"      # 通常包含在基础包中
    "xecjk"      # 检查 xeCJK 相关包
)

for pkg in "${PACKAGES[@]}"; do
    check_and_install "$pkg"
done

echo ""
echo "运行 mktexlsr 更新文件索引..."
sudo mktexlsr

echo ""
echo "============================================"
echo "✅ 检查完成！"
echo "============================================"
echo ""
echo "现在可以尝试编译："
echo "  make thesis"

