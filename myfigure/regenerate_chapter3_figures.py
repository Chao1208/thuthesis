#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
重新生成第三章的图表 - 增大字体以提高可读性
"""

import matplotlib.pyplot as plt
import numpy as np
import os

# 设置中文字体和样式 - 增大所有字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'STHeiti']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.size'] = 13  # 增大基础字体
plt.rcParams['axes.labelsize'] = 16  # 增大轴标签
plt.rcParams['axes.titlesize'] = 18  # 增大标题
plt.rcParams['xtick.labelsize'] = 13  # 增大刻度标签
plt.rcParams['ytick.labelsize'] = 13
plt.rcParams['legend.fontsize'] = 13  # 增大图例

output_dir = os.path.dirname(os.path.abspath(__file__))

# 专业配色方案
COLORS = {
    'primary': '#2E86AB',
    'secondary': '#A23B72',
    'tertiary': '#F18F01',
    'success': '#06A77D',
}

print("="*70)
print("开始重新生成第三章图表（增大字体版本）...")
print("="*70)

# ====================================================================================
# 图3.1：中国互联网网民规模与互联网企业数量增长趋势（2000-2010）
# ====================================================================================
plt.figure(figsize=(14, 9))  # 增大画布

years = np.array([2000, 2002, 2004, 2006, 2008, 2010])
netizens = np.array([0.23, 0.59, 0.94, 1.37, 2.98, 4.57])  # 亿人
companies = np.array([1000, 2500, 5000, 9500, 15000, 20000])  # 家

fig, ax1 = plt.subplots(figsize=(14, 9))

# 网民规模（左轴）
color = COLORS['primary']
ax1.set_xlabel('年份', fontsize=17, fontweight='bold')
ax1.set_ylabel('网民规模（亿人）', fontsize=17, fontweight='bold', color=color)
line1 = ax1.plot(years, netizens, color=color, linewidth=4, marker='o', markersize=12, 
                label='网民规模', markeredgewidth=2, markeredgecolor='white')
ax1.tick_params(axis='y', labelcolor=color, labelsize=14)
ax1.tick_params(axis='x', labelsize=14)
ax1.set_ylim(0, 5)
ax1.grid(True, alpha=0.3, linestyle='--', linewidth=1.5)

# 在数据点上标注数值 - 更大字体
for x, y in zip(years, netizens):
    ax1.annotate(f'{y:.2f}亿', xy=(x, y), xytext=(0, 12),
                textcoords='offset points', ha='center',
                fontsize=12, fontweight='bold', color=color)  # 增大字体

# 企业数量（右轴）
ax2 = ax1.twinx()
color = COLORS['tertiary']
ax2.set_ylabel('互联网企业数量（家）', fontsize=17, fontweight='bold', color=color)
line2 = ax2.plot(years, companies, color=color, linewidth=4, marker='s', markersize=12,
                label='企业数量', markeredgewidth=2, markeredgecolor='white')
ax2.tick_params(axis='y', labelcolor=color, labelsize=14)
ax2.set_ylim(0, 22000)

# 在数据点上标注数值
for x, y in zip(years, companies):
    ax2.annotate(f'{y:,}', xy=(x, y), xytext=(0, -20),
                textcoords='offset points', ha='center',
                fontsize=12, fontweight='bold', color=color)

# 标题和图例
plt.title('中国互联网网民规模与企业数量增长趋势（2000-2010）', 
         fontsize=22, fontweight='bold', pad=25)

# 合并图例 - 增大
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', 
          fontsize=15, frameon=True, shadow=True)

# 添加注释
plt.text(0.5, -0.12, '数据来源：CNNIC中国互联网络发展状况统计报告、工信部统计数据',
        transform=ax1.transAxes, ha='center', fontsize=11, 
        style='italic', color='gray')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'internet-development-2000-2010.pdf'), 
           bbox_inches='tight', dpi=300)
print("✓ 已生成图3.1: internet-development-2000-2010.pdf (字体已增大)")
plt.close()

# ====================================================================================
# 图3.2：中国互联网百强企业研发投入增长趋势（2010-2020）
# ====================================================================================
plt.figure(figsize=(14, 9))

years = np.array([2010, 2012, 2014, 2016, 2018, 2020])
investment = np.array([380, 620, 890, 1150, 1560, 1898])  # 亿元
growth_rate = np.array([28, 35, 25, 22, 27, 21])  # %

fig, ax1 = plt.subplots(figsize=(14, 9))

# 研发投入（左轴，柱状图）
color = COLORS['secondary']
ax1.set_xlabel('年份', fontsize=17, fontweight='bold')
ax1.set_ylabel('研发投入（亿元）', fontsize=17, fontweight='bold', color=color)
bars = ax1.bar(years, investment, color=color, alpha=0.8, width=1.2, 
              edgecolor='white', linewidth=2, label='研发投入')
ax1.tick_params(axis='y', labelcolor=color, labelsize=14)
ax1.tick_params(axis='x', labelsize=14)
ax1.set_ylim(0, 2200)
ax1.grid(True, alpha=0.3, linestyle='--', linewidth=1.5, axis='y')

# 在柱子上标注数值
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height:.0f}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 8),
                textcoords="offset points",
                ha='center', va='bottom',
                fontsize=13, fontweight='bold', color=color)

# 增长率（右轴，折线图）
ax2 = ax1.twinx()
color2 = COLORS['tertiary']
ax2.set_ylabel('同比增长率（%）', fontsize=17, fontweight='bold', color=color2)
line = ax2.plot(years, growth_rate, color=color2, linewidth=4, 
               marker='D', markersize=12, label='增长率',
               markeredgewidth=2, markeredgecolor='white')
ax2.tick_params(axis='y', labelcolor=color2, labelsize=14)
ax2.set_ylim(0, 40)

# 在数据点上标注数值
for x, y in zip(years, growth_rate):
    ax2.annotate(f'{y}%', xy=(x, y), xytext=(0, 12),
                textcoords='offset points', ha='center',
                fontsize=12, fontweight='bold', color=color2)

# 标题和图例
plt.title('中国互联网百强企业研发投入增长趋势（2010-2020）', 
         fontsize=22, fontweight='bold', pad=25)

# 合并图例
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left',
          fontsize=15, frameon=True, shadow=True)

# 添加注释
plt.text(0.5, -0.12, '数据来源：中国互联网协会、工信部《中国互联网企业100强分析报告》',
        transform=ax1.transAxes, ha='center', fontsize=11,
        style='italic', color='gray')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'rnd-investment-growth.pdf'),
           bbox_inches='tight', dpi=300)
print("✓ 已生成图3.2: rnd-investment-growth.pdf (字体已增大)")
plt.close()

# ====================================================================================
# 图3.3：敏捷开发方法应用率变化（2010-2023）
# ====================================================================================
plt.figure(figsize=(14, 9))

years = np.array([2010, 2012, 2014, 2016, 2018, 2020, 2022, 2023])
agile_rate = np.array([15, 22, 35, 52, 68, 78, 80, 82])  # %
devops_rate = np.array([5, 10, 18, 28, 45, 65, 70, 72])  # %

plt.plot(years, agile_rate, color=COLORS['primary'], linewidth=4, 
        marker='o', markersize=14, label='敏捷开发应用率',
        markeredgewidth=2.5, markeredgecolor='white')
plt.plot(years, devops_rate, color=COLORS['success'], linewidth=4,
        marker='s', markersize=14, label='DevOps应用率',
        markeredgewidth=2.5, markeredgecolor='white')

# 标注关键数据点 - 更大字体
for i in [0, 3, 7]:  # 2010, 2016, 2023
    plt.annotate(f'{agile_rate[i]}%', 
                xy=(years[i], agile_rate[i]), 
                xytext=(0, 12),
                textcoords='offset points', 
                ha='center',
                fontsize=13, fontweight='bold', 
                color=COLORS['primary'])
    plt.annotate(f'{devops_rate[i]}%', 
                xy=(years[i], devops_rate[i]), 
                xytext=(0, -20),
                textcoords='offset points', 
                ha='center',
                fontsize=13, fontweight='bold', 
                color=COLORS['success'])

plt.xlabel('年份', fontsize=17, fontweight='bold')
plt.ylabel('应用率（%）', fontsize=17, fontweight='bold')
plt.title('敏捷开发与DevOps方法应用率变化（2010-2023）', 
         fontsize=22, fontweight='bold', pad=20)
plt.legend(fontsize=16, loc='upper left', frameon=True, shadow=True)
plt.grid(True, alpha=0.3, linestyle='--', linewidth=1.5)
plt.ylim(0, 90)
plt.xticks(years, fontsize=14)
plt.yticks(fontsize=14)

# 添加注释
plt.text(0.5, -0.10, '数据来源：IDC《中国敏捷和DevOps软件市场研究报告》',
        transform=plt.gca().transAxes, ha='center', fontsize=11,
        style='italic', color='gray')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'agile-adoption-rate.pdf'),
           bbox_inches='tight', dpi=300)
print("✓ 已生成图3.3: agile-adoption-rate.pdf (字体已增大)")
plt.close()

# ====================================================================================
# 图3.4：互联网企业创新激励机制构成（2023）
# ====================================================================================
plt.figure(figsize=(13, 10))

categories = ['物质激励', '精神激励', '发展激励', '环境激励']
subcategories = [
    ['薪酬奖金\n68%', '股权激励\n58%', '项目奖金\n62%'],
    ['技术表彰\n72%', '技术分享\n85%', '技术竞赛\n48%'],
    ['技术晋升\n92%', '培训机会\n78%', '轮岗机制\n35%'],
    ['创新时间\n35%', '创新基金\n52%', '孵化支持\n28%']
]

# 设置子图
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('互联网企业创新激励机制构成（2023）', 
            fontsize=24, fontweight='bold', y=0.98)

colors_palette = [COLORS['primary'], COLORS['secondary'], 
                 COLORS['tertiary'], COLORS['success']]

for idx, (ax, category, subs, color) in enumerate(zip(axes.flatten(), 
                                                       categories, 
                                                       subcategories, 
                                                       colors_palette)):
    # 提取百分比数据
    values = []
    labels = []
    for sub in subs:
        parts = sub.split('\n')
        labels.append(parts[0])
        values.append(int(parts[1].strip('%')))
    
    # 绘制条形图
    bars = ax.barh(labels, values, color=color, alpha=0.8, 
                  edgecolor='white', linewidth=2.5)
    
    # 添加数值标签 - 更大字体
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 2, bar.get_y() + bar.get_height()/2,
               f'{width}%',
               ha='left', va='center', fontsize=14, 
               fontweight='bold', color=color)
    
    ax.set_xlabel('应用率（%）', fontsize=15, fontweight='bold')
    ax.set_title(category, fontsize=18, fontweight='bold', 
                color=color, pad=15)
    ax.set_xlim(0, 100)
    ax.grid(True, alpha=0.3, axis='x', linestyle='--', linewidth=1.5)
    ax.tick_params(labelsize=13)

# 添加总体说明
fig.text(0.5, 0.02, 
        '数据来源：麦肯锡《中国互联网企业创新管理调研报告2023》、IDC研究',
        ha='center', fontsize=11, style='italic', color='gray')

plt.tight_layout(rect=[0, 0.03, 1, 0.96])
plt.savefig(os.path.join(output_dir, 'innovation-incentive-system.pdf'),
           bbox_inches='tight', dpi=300)
print("✓ 已生成图3.4: innovation-incentive-system.pdf (字体已增大)")
plt.close()

print("="*70)
print("所有图表重新生成完成！")
print("改进：")
print("  • 基础字体从10增大到13")
print("  • 标题字体从14-16增大到18-22")
print("  • 数据标签从9增大到12-13")
print("  • 图例字体从11增大到13-16")
print("  • 线条和标记增大20-30%")
print("  • 画布尺寸增大20-30%")
print("="*70)
print("生成的文件：")
print("  1. internet-development-2000-2010.pdf（优化版）")
print("  2. rnd-investment-growth.pdf（优化版）")
print("  3. agile-adoption-rate.pdf（优化版）")
print("  4. innovation-incentive-system.pdf（优化版）")
print("="*70)

