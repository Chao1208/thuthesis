# 依赖安装指南

本指南将帮助您安装编译 ThuThesis 模板所需的所有依赖项。

## 系统要求

- macOS（已检测到）
- Python 3（已安装 ✓）

## 需要安装的依赖

1. **LaTeX 发行版**（包含 XeTeX/XeLaTeX）
2. **latexmk**（LaTeX 编译工具）
3. **l3build**（LaTeX3 构建工具）

## 安装方式

### 方式 1：使用 Homebrew 安装 BasicTeX（推荐，精简版）

如果您还没有安装 Homebrew，先安装它：

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

然后安装 BasicTeX：

```bash
brew install --cask basictex
```

安装完成后，**需要重新打开终端**或执行：

```bash
eval "$(/usr/libexec/path_helper)"
```

然后安装所需的 LaTeX 包：

```bash
sudo tlmgr update --self
sudo tlmgr install latexmk l3build xetex xelatex
```

### 方式 2：安装完整的 MacTeX（约 4GB）

访问 [MacTeX 官网](https://www.tug.org/mactex/) 下载并安装完整的 MacTeX 发行版。它包含了所有必需的工具和包。

安装后同样需要安装一些额外的包：

```bash
sudo tlmgr update --self
sudo tlmgr install latexmk l3build
```

### 方式 3：手动验证安装

安装完成后，可以验证工具是否正确安装：

```bash
xetex --version
xelatex --version
latexmk --version
l3build --version
```

## 验证安装

安装完成后，您可以尝试编译模板：

```bash
make cls    # 生成 .cls 文件
make doc    # 生成文档
make thesis # 生成示例论文
```

## 常见问题

### 问题：找不到 `tlmgr` 命令

**解决**：安装 BasicTeX 或 MacTeX 后，需要重新打开终端或执行：
```bash
eval "$(/usr/libexec/path_helper)"
```

### 问题：编译时缺少某些 LaTeX 包

**解决**：使用 `tlmgr` 安装缺失的包：
```bash
sudo tlmgr install <包名>
```

如果遇到包缺失错误，模板会提示具体缺少哪个包，您可以按需安装。




