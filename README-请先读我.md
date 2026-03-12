# 清华大学论文模板 - 快速开始指南

## 当前状态

- ✅ Makefile 已配置为编译 `my-thesis.tex`
- ✅ `my-thesis.tex` 已配置为使用 `fandol` 开源字体
- ⚠️ 需要安装缺失的 LaTeX 包

## 一键解决所有问题

在终端运行（需要输入管理员密码）：

```bash
./一键完整安装.sh
```

这个脚本会：
1. 安装所有缺失的 LaTeX 包（bibunits, tex-gyre, xits 等）
2. 清理旧的编译文件
3. 确保 my-thesis.tex 存在并配置正确
4. 自动编译论文
5. 显示编译结果

## 手动安装（如果一键脚本失败）

### 步骤 1: 安装缺失的包

```bash
export PATH="/Library/TeX/texbin:$PATH"
sudo tlmgr install bibunits tex-gyre tex-gyre-math xits
sudo mktexlsr
```

### 步骤 2: 清理并编译

```bash
make clean
make thesis
```

## 缺失包说明

| 包名 | 用途 | 说明 |
|------|------|------|
| `bibunits` | 参考文献管理 | 支持多个独立的参考文献列表 |
| `tex-gyre` | 西文字体 | TeX Gyre 字体系列 |
| `tex-gyre-math` | 数学字体 | TeX Gyre 数学扩展 |
| `xits` | 数学字体 | XITS Math 高质量数学字体 |

## 验证安装

安装完成后，验证包是否安装成功：

```bash
export PATH="/Library/TeX/texbin:$PATH"
kpsewhich bibunits.sty
kpsewhich texgyretermes-regular.otf
kpsewhich xits-math.otf
```

如果都返回文件路径，说明安装成功。

## 编译论文

```bash
make thesis
```

成功后会生成 `my-thesis.pdf`。

## 修改论文内容

- **基本信息**: 编辑 `thusetup.tex`（标题、作者、导师等）
- **论文内容**: 编辑 `data/` 目录下的文件
  - `abstract.tex` - 摘要
  - `chap01.tex` - 第一章
  - `chap02.tex` - 第二章
  - 等等...
- **参考文献**: 编辑 `ref/refs.bib`

## 常见问题

### Q: 提示缺少某个包

A: 查找并安装：
```bash
tlmgr search --global --file <包名>.sty
sudo tlmgr install <找到的包名>
```

### Q: 编译卡住不动

A: 
1. 按 Ctrl+C 中止
2. 运行 `make clean`
3. 再次运行 `make thesis`

### Q: 提示找不到字体

A: 运行一键安装脚本：`./一键完整安装.sh`

## 获取帮助

- 查看详细文档：`README.md`
- 查看模板文档：`thuthesis.pdf`（需要先生成）
- GitHub Issues: https://github.com/tuna/thuthesis/issues

