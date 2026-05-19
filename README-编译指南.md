# thuthesis 编译完整指南

## 问题根源

BasicTeX 是精简版 LaTeX 发行版，只包含基础包。thuthesis 模板需要很多额外的包，导致编译时频繁出现 "File not found" 错误。

## 根本解决方案

### 方案 1：安装所有依赖包（推荐）

运行一键安装脚本：

```bash
./install-all-dependencies.sh
```

这个脚本会安装模板所需的所有包，包括：
- 中文支持包（ctex, xeCJK 等）
- 模板核心包（titletoc, notoccite, geometry 等）
- 示例文件使用的包（algorithm, siunitx 等）

### 方案 2：使用完整版 MacTeX

如果 BasicTeX 经常缺少包，可以考虑安装完整版：

```bash
brew install --cask mactex
```

**注意**：完整版约 4GB，下载和安装时间较长。

## 编译论文

### 使用 Makefile（推荐）

```bash
# 编译 my-thesis.tex
make thesis

# 清理中间文件
make clean

# 清理所有文件（包括 PDF）
make cleanall
```

### 使用编译脚本

```bash
./compile.sh my-thesis
```

## 常见问题

### Q: 编译时提示缺少某个包

A: 运行完整安装脚本：
```bash
./install-all-dependencies.sh
```

如果还缺少，可以使用 tlmgr 单独安装：
```bash
export PATH="/Library/TeX/texbin:$PATH"
sudo tlmgr install <package-name>
```

### Q: make thesis 报错说找不到文件

A: 检查 Makefile 中的 `THESIS` 变量是否正确设置。默认是 `my-thesis`。

### Q: 编译卡住不动

A: 可能是字体加载问题。尝试：
1. 清理中间文件：`make clean`
2. 检查系统字体是否完整
3. 使用 `./compile.sh` 脚本，它会在出错时停止

## 项目文件说明

- `my-thesis.tex` - 你的论文主文件
- `thusetup.tex` - 论文配置（标题、作者等信息）
- `data/` - 论文内容文件（章节、摘要等）
- `ref/refs.bib` - 参考文献
- `figures/` - 图片文件

## 编译流程

1. **填写基本信息**：编辑 `thusetup.tex`
2. **填写论文内容**：编辑 `data/` 目录下的文件
3. **安装依赖**：运行 `./install-all-dependencies.sh`
4. **编译论文**：运行 `make thesis`
5. **查看结果**：打开 `my-thesis.pdf`

## 提示

- 首次编译可能需要较长时间
- 如果修改了参考文献，需要运行多次编译（latexmk 会自动处理）
- 最终提交前建议使用 Windows 平台字体编译（在 thusetup.tex 中设置 `fontset = windows`）

