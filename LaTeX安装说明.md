# LaTeX 安装说明

## 问题
编译时出现错误：`xetex: command not found`

## 解决方案

### 方法 1：使用 Homebrew 安装 BasicTeX（推荐）

在你的终端中运行：

```bash
brew install --cask basictex
```

安装完成后，**重新打开终端**或运行：

```bash
eval "$(/usr/libexec/path_helper)"
```

### 方法 2：直接运行已下载的安装包

安装包已经下载到本地，可以直接安装：

```bash
sudo installer -pkg /Users/lichao/Library/Caches/Homebrew/downloads/05fd531fa80e17c933948112bf43c62972af81923dae576d2c88ceb9a7c87c30--mactex-basictex-20250308.pkg -target /
```

### 验证安装

安装完成后，验证是否成功：

```bash
# 配置路径（如果还没重新打开终端）
eval "$(/usr/libexec/path_helper)"

# 检查 xelatex 是否可用
which xelatex
xelatex --version
```

### 编译论文

安装完成后，回到项目目录，运行：

```bash
cd /Users/lichao/Documents/project/github/thuthesis
make thesis
```

或者如果使用 `my-thesis.tex`：

```bash
latexmk my-thesis
```

## 注意事项

1. **需要管理员密码**：安装过程中会提示输入你的 Mac 登录密码
2. **BasicTeX 是精简版**：如果编译时缺少某些包，可以使用 `tlmgr` 安装：
   ```bash
   sudo tlmgr update --self
   sudo tlmgr install <package-name>
   ```
3. **完整版 MacTeX**：如果需要完整版（约 4GB），可以使用：
   ```bash
   brew install --cask mactex
   ```
   但通常 BasicTeX 已经足够使用。

## 如果仍然遇到问题

1. 确保已重新打开终端或运行 `eval "$(/usr/libexec/path_helper)"`
2. 检查路径：`echo $PATH` 应该包含 `/Library/TeX/texbin`
3. 如果路径不对，可以将以下内容添加到 `~/.zshrc`：
   ```bash
   export PATH="/Library/TeX/texbin:$PATH"
   ```

