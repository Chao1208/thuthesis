#!/usr/bin/env python3
"""生成第3章剩余2张图"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

OUT = os.path.dirname(os.path.abspath(__file__))

plt.rcParams.update({
    'font.family': ['PingFang HK', 'Heiti TC', 'Arial Unicode MS', 'sans-serif'],
    'axes.unicode_minus': False,
    'font.size': 11,
})

# ─────────────────────────────────────────────
# 1. tab:ai-impact-summary → 热力矩阵/气泡图
# ─────────────────────────────────────────────
def gen_ai_impact():
    dims = ['开发效率', '技能需求', '产品形态', '技术架构', '战略选择', '人才竞争', '伦理合规']
    # 影响程度(1-5) / 变化速度(1-5)
    impact  = [4.5, 4.0, 4.5, 3.5, 4.0, 5.0, 3.5]
    speed   = [4.5, 3.5, 4.0, 3.0, 3.5, 5.0, 3.0]
    # 气泡大小：关键数据量化影响
    sizes   = [300, 200, 280, 180, 220, 380, 160]
    colors  = ['#2563EB','#16A34A','#7C3AED','#D97706','#0891B2','#DC2626','#6B7280']
    labels_detail = [
        '效率+30~50%\n100万+用户',
        '65%必备\n18%掌握',
        'AI Native\n产品兴起',
        '单次训练\n百万~千万',
        '68%混合\n策略',
        '缺口100万\n供需1:10',
        '85%需合规\n周期+20~40%',
    ]

    fig, ax = plt.subplots(figsize=(9, 6))
    for i, (dim, imp, spd, sz, col, lbl) in enumerate(
            zip(dims, impact, speed, sizes, colors, labels_detail)):
        sc = ax.scatter(imp, spd, s=sz, color=col, alpha=0.75, edgecolors='white', linewidths=1.5, zorder=3)
        ax.annotate(dim, (imp, spd), textcoords='offset points', xytext=(0, 10),
                    ha='center', fontsize=9.5, fontweight='bold', color=col)
        ax.annotate(lbl, (imp, spd), textcoords='offset points', xytext=(0, -22),
                    ha='center', fontsize=7.5, color='#555555')

    ax.set_xlim(2.5, 5.5)
    ax.set_ylim(2.0, 5.5)
    ax.set_xlabel('影响程度', fontsize=12)
    ax.set_ylabel('变化速度', fontsize=12)
    ax.set_title('生成式AI对互联网研发管理的多维度影响分布', fontsize=13, fontweight='bold', pad=12)
    ax.axvline(x=4.0, color='gray', linestyle='--', lw=1, alpha=0.5)
    ax.axhline(y=3.75, color='gray', linestyle='--', lw=1, alpha=0.5)
    ax.text(4.7, 5.25, '高影响·快变化', fontsize=9, color='#DC2626', style='italic')
    ax.text(2.7, 5.25, '低影响·快变化', fontsize=9, color='#6B7280', style='italic')
    ax.text(4.7, 2.15, '高影响·慢变化', fontsize=9, color='#D97706', style='italic')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    for ext in ('pdf', 'png'):
        plt.savefig(os.path.join(OUT, f'ai-impact-summary.{ext}'), dpi=150, bbox_inches='tight')
    plt.close()
    print("ai-impact-summary done")

# ─────────────────────────────────────────────
# 2. tab:devops-metrics-comparison → 分组柱状图
# ─────────────────────────────────────────────
def gen_devops_comparison():
    metrics = ['部署频率\n(次/月)', '交付周期\n(天)', '故障恢复\n(小时)', '变更失败率\n(%)', '自动化率\n(%)']
    traditional = [1.5,  37.5, 6.0, 17.5, 40]
    devops      = [30,   10.5, 1.25, 6.5,  85]
    # 归一化到0-100用于对比显示（部署频率/自动化率越高越好；其余越低越好）
    # 直接用原始值，但分开展示
    x = np.arange(len(metrics))
    width = 0.32

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # 左图：绝对值对比
    ax = axes[0]
    b1 = ax.bar(x - width/2, traditional, width, label='传统模式', color='#F87171', alpha=0.85)
    b2 = ax.bar(x + width/2, devops,      width, label='DevOps模式', color='#34D399', alpha=0.85)
    ax.set_xticks(x)
    ax.set_xticklabels(metrics, fontsize=9)
    ax.set_ylabel('原始数值', fontsize=10)
    ax.set_title('DevOps实践前后关键指标对比（绝对值）', fontsize=11, fontweight='bold')
    ax.legend(fontsize=9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    for bar in b1:
        h = bar.get_height()
        ax.text(bar.get_x()+bar.get_width()/2, h+0.5, f'{h}', ha='center', va='bottom', fontsize=7.5)
    for bar in b2:
        h = bar.get_height()
        ax.text(bar.get_x()+bar.get_width()/2, h+0.5, f'{h}', ha='center', va='bottom', fontsize=7.5)

    # 右图：提升幅度
    ax2 = axes[1]
    improvements = ['部署频率\n提升20倍', '交付周期\n缩短72%', '故障恢复\n缩短79%', '变更失败率\n降低63%', '自动化率\n提升113%']
    imp_values   = [20, 72, 79, 63, 113]  # 倍数或百分比
    colors_imp   = ['#2563EB','#16A34A','#16A34A','#16A34A','#7C3AED']
    bars = ax2.barh(improvements, imp_values, color=colors_imp, alpha=0.82)
    ax2.set_xlabel('改善幅度 (%或倍数)', fontsize=10)
    ax2.set_title('DevOps实践效益汇总', fontsize=11, fontweight='bold')
    for bar, val in zip(bars, imp_values):
        ax2.text(val+0.5, bar.get_y()+bar.get_height()/2,
                 f'{val}{"×" if val==20 else "%"}',
                 va='center', fontsize=9.5, fontweight='bold')
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)

    plt.suptitle('互联网企业DevOps实践效益分析', fontsize=13, fontweight='bold', y=1.02)
    plt.tight_layout()
    for ext in ('pdf', 'png'):
        plt.savefig(os.path.join(OUT, f'devops-metrics-comparison.{ext}'), dpi=150, bbox_inches='tight')
    plt.close()
    print("devops-metrics-comparison done")

if __name__ == '__main__':
    gen_ai_impact()
    gen_devops_comparison()
    print("All done.")
