# 第四章图表说明

## 已添加的图表引用

### 图4-1: baidu-org-evolution.pdf
- **位置**: §4.2.1 研发组织架构与组织调整路径
- **内容**: 百度研发组织架构演变（烟囱式 vs BMU/AMU双BU架构）
- **脚本**: generate_chapter4_simple.py 中的 create_org_evolution()

### 图4-2: swot-radar-baidu.pdf
- **位置**: §4.3.2 问题产生的原因分析——基于量化SWOT框架
- **内容**: SWOT战略四象限雷达图（SO/WO/WT/ST）
- **脚本**: generate_chapter4_simple.py 中的 create_swot_radar()

### 图4-3: amo-comparison.pdf
- **位置**: §4.3.3 运用AMO框架的深入分析
- **内容**: AMO三维对比热力图（百度 vs 行业标杆）
- **脚本**: generate_chapter4_simple.py 中的 create_amo_comparison()

### 图4-4: dual-career-channel.pdf
- **位置**: §4.4.2 激励机制创新
- **内容**: 双通道职业发展体系（管理通道 vs 技术通道）
- **脚本**: generate_chapter4_simple.py 中的 create_dual_channel()

### 图4-5: rd-effectiveness-dashboard.pdf
- **位置**: §4.4.3 团队绩效提升方法
- **内容**: 研发效能综合仪表盘（6个核心指标面板）
- **脚本**: generate_chapter4_simple.py 中的 create_rd_dashboard()

### 图4-6: pdca-improvement.pdf
- **位置**: §4.4.3 团队绩效提升方法
- **内容**: PDCA持续改进循环图
- **脚本**: generate_chapter4_simple.py 中的 create_pdca()

## 图表生成方法

### 方法1: 使用Python脚本（推荐）
```bash
cd myfigure
python3 generate_chapter4_simple.py
```

如果字体有问题，可以尝试安装中文字体或修改脚本中的字体设置。

### 方法2: 使用LaTeX TikZ直接绘制
可以在.tex文件中使用tikz包直接绘制这些图表，例如：

```latex
\begin{figure}[htbp]
\centering
\begin{tikzpicture}
% 绘制SWOT雷达图等
\end{tikzpicture}
\caption{...}
\end{figure}
```

### 方法3: 使用外部工具
- 使用PowerPoint/Keynote绘制后导出PDF
- 使用draw.io等在线工具
- 使用Matlab/Python Jupyter Notebook

## 已有波特五力图

图4-0: porter-five-forces-baidu.pdf 已存在，用于§4.1.4节。

---

**注意**: 运行脚本需要安装matplotlib和numpy：
```bash
pip3 install matplotlib numpy
```
