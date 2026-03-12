#!/bin/bash

# 安装 latexmk 脚本
echo "正在安装 latexmk..."
echo "注意：安装过程中需要输入管理员密码"

export PATH="/Library/TeX/texbin:$PATH"
sudo tlmgr install latexmk

echo "安装完成！现在可以运行 make thesis 了"

