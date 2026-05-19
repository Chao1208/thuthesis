#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
重新生成所有图表 - 移除底部数据来源标注
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import matplotlib.lines as mlines
import numpy as np
import os

# 设置中文字体和样式
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'STHeiti']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.size'] = 14
plt.rcParams['axes.labelsize'] = 16
plt.rcParams['axes.titlesize'] = 20
plt.rcParams['xtick.labelsize'] = 13
plt.rcParams['ytick.labelsize'] = 13
plt.rcParams['legend.fontsize'] = 14

output_dir = os.path.dirname(os.path.abspath(__file__))

# 专业配色方案
COLORS = {
    'primary': '#2E86AB',
    'secondary': '#A23B72',
    'tertiary': '#F18F01',
    'success': '#06A77D',
    'warning': '#D2691E',
    'info': '#4682B4',
    'purple': '#7B68EE'
}

print("="*70)
print("开始重新生成所有图表（移除数据来源标注）...")
print("="*70)

# ====================================================================================
# 第二章 - 图2.1：AMO框架图
# ====================================================================================
fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# 中心圆 - 员工绩效
center_circle = Circle((5, 5), 1.2, 
                      facecolor=COLORS['primary'], 
                      edgecolor='white',
                      linewidth=3,
                      alpha=0.9)
ax.add_patch(center_circle)
ax.text(5, 5, '员工\n绩效', 
       ha='center', va='center',
       fontsize=22, fontweight='bold', color='white')

# 三个要素圆
# Ability - 能力
ability_circle = Circle((2.5, 7.5), 1, 
                       facecolor=COLORS['secondary'], 
                       edgecolor='white',
                       linewidth=2.5,
                       alpha=0.85)
ax.add_patch(ability_circle)
ax.text(2.5, 7.8, '能力', 
       ha='center', va='center',
       fontsize=20, fontweight='bold', color='white')
ax.text(2.5, 7.2, 'Ability', 
       ha='center', va='center',
       fontsize=15, color='white', style='italic')

# Motivation - 动机
motivation_circle = Circle((7.5, 7.5), 1, 
                          facecolor=COLORS['tertiary'], 
                          edgecolor='white',
                          linewidth=2.5,
                          alpha=0.85)
ax.add_patch(motivation_circle)
ax.text(7.5, 7.8, '动机', 
       ha='center', va='center',
       fontsize=20, fontweight='bold', color='white')
ax.text(7.5, 7.2, 'Motivation', 
       ha='center', va='center',
       fontsize=15, color='white', style='italic')

# Opportunity - 机会
opportunity_circle = Circle((5, 2.5), 1, 
                           facecolor=COLORS['success'], 
                           edgecolor='white',
                           linewidth=2.5,
                           alpha=0.85)
ax.add_patch(opportunity_circle)
ax.text(5, 2.8, '机会', 
       ha='center', va='center',
       fontsize=20, fontweight='bold', color='white')
ax.text(5, 2.2, 'Opportunity', 
       ha='center', va='center',
       fontsize=15, color='white', style='italic')

# 添加箭头连接
arrow_props = dict(
    arrowstyle='->',
    lw=3,
    alpha=0.7,
    mutation_scale=25
)

ax.annotate('', xy=(4.2, 5.8), xytext=(3.2, 6.8),
            arrowprops={**arrow_props, 'color': COLORS['secondary']})
ax.annotate('', xy=(5.8, 5.8), xytext=(6.8, 6.8),
            arrowprops={**arrow_props, 'color': COLORS['tertiary']})
ax.annotate('', xy=(5, 3.7), xytext=(5, 3.5),
            arrowprops={**arrow_props, 'color': COLORS['success']})

# 添加详细说明
ability_text = ['• 知识水平', '• 技能熟练度', '• 专业能力', '• 学习能力']
y_pos = 9.3
for text in ability_text:
    ax.text(2.5, y_pos, text,
           ha='center', va='center',
           fontsize=12, color=COLORS['secondary'],
           bbox=dict(boxstyle='round,pad=0.4', 
                    facecolor='white', 
                    edgecolor=COLORS['secondary'],
                    alpha=0.8))
    y_pos -= 0.35

motivation_text = ['• 内在动机', '• 外在激励', '• 工作热情', '• 目标导向']
y_pos = 9.3
for text in motivation_text:
    ax.text(7.5, y_pos, text,
           ha='center', va='center',
           fontsize=12, color=COLORS['tertiary'],
           bbox=dict(boxstyle='round,pad=0.4', 
                    facecolor='white', 
                    edgecolor=COLORS['tertiary'],
                    alpha=0.8))
    y_pos -= 0.35

opportunity_text = ['• 参与决策', '• 资源支持', '• 成长机会', '• 工作自主性']
x_pos = 2.8
for text in opportunity_text:
    ax.text(x_pos, 1.2, text,
           ha='center', va='center',
           fontsize=12, color=COLORS['success'],
           bbox=dict(boxstyle='round,pad=0.4', 
                    facecolor='white', 
                    edgecolor=COLORS['success'],
                    alpha=0.8))
    x_pos += 1.5

plt.title('AMO框架：员工绩效的三要素模型', 
         fontsize=24, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'amo-framework.pdf'), 
           bbox_inches='tight', dpi=300,
           facecolor='white', edgecolor='none')
print("✓ 已生成图2.1: amo-framework.pdf")
plt.close()

# ====================================================================================
# 第二章 - 图2.2：IMOI团队效能模型
# ====================================================================================
fig, ax = plt.subplots(figsize=(16, 7))
ax.set_xlim(0, 14)
ax.set_ylim(0, 6)
ax.axis('off')

stages = [
    {'x': 0.5, 'y': 2, 'w': 2.5, 'h': 2, 'title': '投入\nInput', 
     'color': COLORS['primary']},
    {'x': 4, 'y': 2, 'w': 2.5, 'h': 2, 'title': '中介\nMediator', 
     'color': COLORS['secondary']},
    {'x': 7.5, 'y': 2, 'w': 2.5, 'h': 2, 'title': '产出\nOutput', 
     'color': COLORS['tertiary']},
    {'x': 11, 'y': 2, 'w': 2.5, 'h': 2, 'title': '再投入\nInput', 
     'color': COLORS['success']}
]

for stage in stages:
    box = FancyBboxPatch(
        (stage['x'], stage['y']), stage['w'], stage['h'],
        boxstyle="round,pad=0.1",
        edgecolor=stage['color'],
        facecolor=stage['color'],
        alpha=0.85,
        linewidth=3
    )
    ax.add_patch(box)
    ax.text(stage['x'] + stage['w']/2, stage['y'] + stage['h']/2, 
           stage['title'],
           ha='center', va='center',
           fontsize=18, fontweight='bold', color='white')

arrow_props = dict(arrowstyle='->', lw=4, alpha=0.8, mutation_scale=30)

ax.annotate('', xy=(4, 3), xytext=(3, 3),
           arrowprops={**arrow_props, 'color': '#666666'})
ax.annotate('', xy=(7.5, 3), xytext=(6.5, 3),
           arrowprops={**arrow_props, 'color': '#666666'})
ax.annotate('', xy=(11, 3), xytext=(10, 3),
           arrowprops={**arrow_props, 'color': '#666666'})
ax.annotate('', xy=(1.75, 1.8), xytext=(12.25, 1.8),
           arrowprops={**arrow_props, 'color': COLORS['warning'],
                      'linestyle': 'dashed', 'lw': 3})

ax.text(7, 1.2, '反馈循环', 
       ha='center', va='center',
       fontsize=15, color=COLORS['warning'],
       fontweight='bold', style='italic')

input_items = ['组织情境', '团队特征', '个体特征']
y_pos = 4.6
for item in input_items:
    ax.text(1.75, y_pos, f'• {item}',
           ha='center', va='center',
           fontsize=12, color='white')
    y_pos += 0.35

mediator_items = ['团队过程', '涌现状态', '协作机制']
y_pos = 4.6
for item in mediator_items:
    ax.text(5.25, y_pos, f'• {item}',
           ha='center', va='center',
           fontsize=12, color='white')
    y_pos += 0.35

output_items = ['团队绩效', '成员满意度', '创新产出']
y_pos = 4.6
for item in output_items:
    ax.text(8.75, y_pos, f'• {item}',
           ha='center', va='center',
           fontsize=12, color='white')
    y_pos += 0.35

plt.title('I-M-O-I团队效能循环模型', 
         fontsize=24, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'imoi-model.pdf'), 
           bbox_inches='tight', dpi=300,
           facecolor='white', edgecolor='none')
print("✓ 已生成图2.2: imoi-model.pdf")
plt.close()

# ====================================================================================
# 第二章 - 图2.3：开放式创新模型
# ====================================================================================
fig, ax = plt.subplots(figsize=(14, 11))
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis('off')

company_box = FancyBboxPatch(
    (3, 3), 6, 4,
    boxstyle="round,pad=0.15",
    edgecolor=COLORS['primary'],
    facecolor=COLORS['primary'],
    alpha=0.2,
    linewidth=4
)
ax.add_patch(company_box)
ax.text(6, 6.5, '企业创新系统', 
       ha='center', va='center',
       fontsize=20, fontweight='bold',
       color=COLORS['primary'])

internal_box = FancyBboxPatch(
    (4.5, 4), 3, 1.8,
    boxstyle="round,pad=0.08",
    edgecolor=COLORS['secondary'],
    facecolor=COLORS['secondary'],
    alpha=0.85,
    linewidth=2.5
)
ax.add_patch(internal_box)
ax.text(6, 5.2, '内部研发', 
       ha='center', va='center',
       fontsize=17, fontweight='bold', color='white')
ax.text(6, 4.6, 'Internal R&D', 
       ha='center', va='center',
       fontsize=13, color='white', style='italic')

external_inputs = [
    {'y': 8.5, 'text': '大学/研究机构', 'color': COLORS['success']},
    {'y': 6.5, 'text': '合作伙伴', 'color': COLORS['tertiary']},
    {'y': 4.5, 'text': '客户/用户', 'color': COLORS['info']},
    {'y': 2.5, 'text': '供应商', 'color': COLORS['warning']}
]

for inp in external_inputs:
    box = FancyBboxPatch(
        (0.3, inp['y']-0.4), 2, 0.8,
        boxstyle="round,pad=0.05",
        edgecolor=inp['color'],
        facecolor=inp['color'],
        alpha=0.8,
        linewidth=2
    )
    ax.add_patch(box)
    ax.text(1.3, inp['y'], inp['text'],
           ha='center', va='center',
           fontsize=13, fontweight='bold', color='white')
    
    ax.annotate('', xy=(3, inp['y']), xytext=(2.3, inp['y']),
               arrowprops=dict(arrowstyle='->', lw=2.5,
                              color=inp['color'], alpha=0.7))

external_outputs = [
    {'y': 8.5, 'text': '技术转让', 'color': COLORS['purple']},
    {'y': 6.5, 'text': '开源项目', 'color': COLORS['secondary']},
    {'y': 4.5, 'text': '产品/服务', 'color': COLORS['tertiary']},
    {'y': 2.5, 'text': '专利许可', 'color': COLORS['primary']}
]

for out in external_outputs:
    box = FancyBboxPatch(
        (9.7, out['y']-0.4), 2, 0.8,
        boxstyle="round,pad=0.05",
        edgecolor=out['color'],
        facecolor=out['color'],
        alpha=0.8,
        linewidth=2
    )
    ax.add_patch(box)
    ax.text(10.7, out['y'], out['text'],
           ha='center', va='center',
           fontsize=13, fontweight='bold', color='white')
    
    ax.annotate('', xy=(9.7, out['y']), xytext=(9, out['y']),
               arrowprops=dict(arrowstyle='->', lw=2.5, 
                              color=out['color'], alpha=0.7))

ax.text(1.3, 9.5, '外部知识输入', 
       ha='center', va='center',
       fontsize=16, fontweight='bold',
       color=COLORS['success'])

ax.text(10.7, 9.5, '创新成果输出', 
       ha='center', va='center',
       fontsize=16, fontweight='bold', 
       color=COLORS['tertiary'])

ax.text(6, 1.5, '↔', 
       ha='center', va='center',
       fontsize=35, color=COLORS['primary'])
ax.text(6, 0.9, '双向流动与协同创新', 
       ha='center', va='center',
       fontsize=15, fontweight='bold',
       color=COLORS['primary'])

plt.title('开放式创新模型（Chesbrough）', 
         fontsize=24, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'open-innovation-model.pdf'), 
           bbox_inches='tight', dpi=300,
           facecolor='white', edgecolor='none')
print("✓ 已生成图2.3: open-innovation-model.pdf")
plt.close()

# ====================================================================================
# 第三章图表
# ====================================================================================

# 设置第三章字体
plt.rcParams['font.size'] = 13
plt.rcParams['axes.labelsize'] = 16
plt.rcParams['axes.titlesize'] = 18
plt.rcParams['xtick.labelsize'] = 13
plt.rcParams['ytick.labelsize'] = 13
plt.rcParams['legend.fontsize'] = 13

# ====================================================================================
# 图3.1：中国互联网网民规模与企业数量增长趋势
# ====================================================================================
years = np.array([2000, 2002, 2004, 2006, 2008, 2010])
netizens = np.array([0.23, 0.59, 0.94, 1.37, 2.98, 4.57])
companies = np.array([1000, 2500, 5000, 9500, 15000, 20000])

fig, ax1 = plt.subplots(figsize=(14, 9))

color = COLORS['primary']
ax1.set_xlabel('年份', fontsize=17, fontweight='bold')
ax1.set_ylabel('网民规模（亿人）', fontsize=17, fontweight='bold', color=color)
line1 = ax1.plot(years, netizens, color=color, linewidth=4, marker='o', markersize=12, 
                label='网民规模', markeredgewidth=2, markeredgecolor='white')
ax1.tick_params(axis='y', labelcolor=color, labelsize=14)
ax1.tick_params(axis='x', labelsize=14)
ax1.set_ylim(0, 5)
ax1.grid(True, alpha=0.3, linestyle='--', linewidth=1.5)

for x, y in zip(years, netizens):
    ax1.annotate(f'{y:.2f}亿', xy=(x, y), xytext=(0, 12),
                textcoords='offset points', ha='center',
                fontsize=12, fontweight='bold', color=color)

ax2 = ax1.twinx()
color = COLORS['tertiary']
ax2.set_ylabel('互联网企业数量（家）', fontsize=17, fontweight='bold', color=color)
line2 = ax2.plot(years, companies, color=color, linewidth=4, marker='s', markersize=12,
                label='企业数量', markeredgewidth=2, markeredgecolor='white')
ax2.tick_params(axis='y', labelcolor=color, labelsize=14)
ax2.set_ylim(0, 22000)

for x, y in zip(years, companies):
    ax2.annotate(f'{y:,}', xy=(x, y), xytext=(0, -20),
                textcoords='offset points', ha='center',
                fontsize=12, fontweight='bold', color=color)

plt.title('中国互联网网民规模与企业数量增长趋势（2000-2010）', 
         fontsize=22, fontweight='bold', pad=25)

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', 
          fontsize=15, frameon=True, shadow=True)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'internet-development-2000-2010.pdf'), 
           bbox_inches='tight', dpi=300)
print("✓ 已生成图3.1: internet-development-2000-2010.pdf")
plt.close()

# ====================================================================================
# 图3.2：研发投入增长趋势
# ====================================================================================
years = np.array([2010, 2012, 2014, 2016, 2018, 2020])
investment = np.array([380, 620, 890, 1150, 1560, 1898])
growth_rate = np.array([28, 35, 25, 22, 27, 21])

fig, ax1 = plt.subplots(figsize=(14, 9))

color = COLORS['secondary']
ax1.set_xlabel('年份', fontsize=17, fontweight='bold')
ax1.set_ylabel('研发投入（亿元）', fontsize=17, fontweight='bold', color=color)
bars = ax1.bar(years, investment, color=color, alpha=0.8, width=1.2, 
              edgecolor='white', linewidth=2, label='研发投入')
ax1.tick_params(axis='y', labelcolor=color, labelsize=14)
ax1.tick_params(axis='x', labelsize=14)
ax1.set_ylim(0, 2200)
ax1.grid(True, alpha=0.3, linestyle='--', linewidth=1.5, axis='y')

for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height:.0f}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 8),
                textcoords="offset points",
                ha='center', va='bottom',
                fontsize=13, fontweight='bold', color=color)

ax2 = ax1.twinx()
color2 = COLORS['tertiary']
ax2.set_ylabel('同比增长率（%）', fontsize=17, fontweight='bold', color=color2)
line = ax2.plot(years, growth_rate, color=color2, linewidth=4, 
               marker='D', markersize=12, label='增长率',
               markeredgewidth=2, markeredgecolor='white')
ax2.tick_params(axis='y', labelcolor=color2, labelsize=14)
ax2.set_ylim(0, 40)

for x, y in zip(years, growth_rate):
    ax2.annotate(f'{y}%', xy=(x, y), xytext=(0, 12),
                textcoords='offset points', ha='center',
                fontsize=12, fontweight='bold', color=color2)

plt.title('中国互联网百强企业研发投入增长趋势（2010-2020）', 
         fontsize=22, fontweight='bold', pad=25)

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left',
          fontsize=15, frameon=True, shadow=True)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'rnd-investment-growth.pdf'),
           bbox_inches='tight', dpi=300)
print("✓ 已生成图3.2: rnd-investment-growth.pdf")
plt.close()

# ====================================================================================
# 图3.3：敏捷开发应用率变化
# ====================================================================================
years = np.array([2010, 2012, 2014, 2016, 2018, 2020, 2022, 2023])
agile_rate = np.array([15, 22, 35, 52, 68, 78, 80, 82])
devops_rate = np.array([5, 10, 18, 28, 45, 65, 70, 72])

plt.figure(figsize=(14, 9))

plt.plot(years, agile_rate, color=COLORS['primary'], linewidth=4, 
        marker='o', markersize=14, label='敏捷开发应用率',
        markeredgewidth=2.5, markeredgecolor='white')
plt.plot(years, devops_rate, color=COLORS['success'], linewidth=4,
        marker='s', markersize=14, label='DevOps应用率',
        markeredgewidth=2.5, markeredgecolor='white')

for i in [0, 3, 7]:
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

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'agile-adoption-rate.pdf'),
           bbox_inches='tight', dpi=300)
print("✓ 已生成图3.3: agile-adoption-rate.pdf")
plt.close()

# ====================================================================================
# 图3.4：创新激励机制构成
# ====================================================================================
categories = ['物质激励', '精神激励', '发展激励', '环境激励']
subcategories = [
    ['薪酬奖金\n68%', '股权激励\n58%', '项目奖金\n62%'],
    ['技术表彰\n72%', '技术分享\n85%', '技术竞赛\n48%'],
    ['技术晋升\n92%', '培训机会\n78%', '轮岗机制\n35%'],
    ['创新时间\n35%', '创新基金\n52%', '孵化支持\n28%']
]

fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('互联网企业创新激励机制构成（2023）', 
            fontsize=24, fontweight='bold', y=0.98)

colors_palette = [COLORS['primary'], COLORS['secondary'], 
                 COLORS['tertiary'], COLORS['success']]

for idx, (ax, category, subs, color) in enumerate(zip(axes.flatten(), 
                                                       categories, 
                                                       subcategories, 
                                                       colors_palette)):
    values = []
    labels = []
    for sub in subs:
        parts = sub.split('\n')
        labels.append(parts[0])
        values.append(int(parts[1].strip('%')))
    
    bars = ax.barh(labels, values, color=color, alpha=0.8, 
                  edgecolor='white', linewidth=2.5)
    
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

plt.tight_layout(rect=[0, 0.01, 1, 0.96])
plt.savefig(os.path.join(output_dir, 'innovation-incentive-system.pdf'),
           bbox_inches='tight', dpi=300)
print("✓ 已生成图3.4: innovation-incentive-system.pdf")
plt.close()

print("="*70)
print("所有图表重新生成完成！")
print("改进：已移除所有图表底部的数据来源标注")
print("="*70)
print("生成的文件：")
print("  第二章图表：")
print("    1. amo-framework.pdf")
print("    2. imoi-model.pdf")
print("    3. open-innovation-model.pdf")
print("  第三章图表：")
print("    4. internet-development-2000-2010.pdf")
print("    5. rnd-investment-growth.pdf")
print("    6. agile-adoption-rate.pdf")
print("    7. innovation-incentive-system.pdf")
print("="*70)

