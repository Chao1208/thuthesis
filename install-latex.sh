#!/bin/bash

# 安装 BasicTeX 脚本
echo "正在安装 BasicTeX..."
echo "注意：安装过程中需要输入管理员密码"

# 使用 Homebrew 安装 BasicTeX
brew install --cask basictex

# 配置路径
echo "配置 LaTeX 路径..."
eval "$(/usr/libexec/path_helper)"

# 验证安装
echo "验证安装..."
if command -v xelatex &> /dev/null; then
    echo "✅ XeLaTeX 安装成功！"
    xelatex --version | head -1
else
    echo "⚠️  请重新打开终端或运行: eval \"\$(/usr/libexec/path_helper)\""
    echo "然后运行: make thesis"
fi

