#!/bin/bash

# ThuThesis 依赖安装脚本
# 适用于 macOS 系统

set -e

echo "=========================================="
echo "ThuThesis 依赖安装脚本"
echo "=========================================="
echo ""

# 检查 Python 3
echo "检查 Python 3..."
if command -v python3 &> /dev/null; then
    echo "✓ Python 3 已安装: $(python3 --version)"
else
    echo "✗ Python 3 未安装，请先安装 Python 3"
    exit 1
fi
echo ""

# 检查是否已安装 LaTeX 工具
check_latex() {
    if command -v xetex &> /dev/null && command -v latexmk &> /dev/null; then
        echo "✓ LaTeX 工具已安装"
        xetex --version | head -n 1
        latexmk --version | head -n 1
        return 0
    else
        return 1
    fi
}

if check_latex; then
    echo ""
    echo "检测到 LaTeX 已安装。检查是否需要安装额外包..."
    
    # 检查 tlmgr 并更新包
    if command -v tlmgr &> /dev/null; then
        echo "检查并安装必要的 LaTeX 包..."
        sudo tlmgr update --self || true
        sudo tlmgr install latexmk l3build || true
        echo "✓ LaTeX 包安装完成"
    fi
    
    echo ""
    echo "=========================================="
    echo "所有依赖已就绪！"
    echo "=========================================="
    exit 0
fi

# 检查 Homebrew
echo "检查 Homebrew..."
if command -v brew &> /dev/null; then
    echo "✓ Homebrew 已安装"
    BREW_AVAILABLE=true
else
    echo "✗ Homebrew 未安装"
    BREW_AVAILABLE=false
fi
echo ""

# 选择安装方式
if [ "$BREW_AVAILABLE" = true ]; then
    echo "检测到 Homebrew，将使用 Homebrew 安装 BasicTeX"
    echo ""
    read -p "是否继续安装？(y/n) " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "正在安装 BasicTeX..."
        brew install --cask basictex
        
        echo ""
        echo "BasicTeX 安装完成！"
        echo "正在配置环境变量..."
        eval "$(/usr/libexec/path_helper)"
        
        echo ""
        echo "正在安装必需的 LaTeX 包..."
        sudo tlmgr update --self
        sudo tlmgr install latexmk l3build collection-xetex
        
        echo ""
        echo "=========================================="
        echo "安装完成！"
        echo "=========================================="
        echo ""
        echo "请重新打开终端或执行以下命令使环境变量生效："
        echo "  eval \"\$(/usr/libexec/path_helper)\""
        echo ""
        echo "然后可以运行以下命令验证安装："
        echo "  xetex --version"
        echo "  latexmk --version"
        echo "  l3build --version"
    else
        echo "已取消安装"
        echo ""
        echo "您可以手动安装："
        echo "1. 访问 https://www.tug.org/mactex/ 下载并安装 MacTeX"
        echo "2. 或使用 Homebrew: brew install --cask basictex"
    fi
else
    echo "未检测到 Homebrew"
    echo ""
    echo "请选择安装方式："
    echo ""
    echo "方式 1：安装 Homebrew + BasicTeX（推荐）"
    echo "  1. 先安装 Homebrew："
    echo "     /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
    echo "  2. 然后运行此脚本 again"
    echo ""
    echo "方式 2：直接安装 MacTeX（完整版，约 4GB）"
    echo "  访问 https://www.tug.org/mactex/ 下载并安装"
    echo ""
    read -p "是否现在安装 Homebrew？(y/n) " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "正在安装 Homebrew..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        echo ""
        echo "Homebrew 安装完成！请重新运行此脚本继续安装 BasicTeX"
    else
        echo "已取消。您可以稍后手动安装依赖"
    fi
fi




