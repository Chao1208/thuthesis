#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成第四章图表（黑白打印版）
- 10pt 宋体 / Times New Roman（figsize=显示宽度，不缩放）
- 8pt 坐标轴刻度
- 纹理区分模块
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np
import os

DISPLAY_W = 5.91
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Songti SC', 'STSong', 'SimSun', 'Times New Roman'],
    'mathtext.fontset': 'stix',
    'axes.unicode_minus': False,
    'figure.dpi': 300,
    'figure.facecolor': 'white',
    'savefig.facecolor': 'white',
    'hatch.linewidth': 0.5,
})

FS = 10
FS_TICK = 8
FS_SMALL = 8


def _tbg():
    return dict(boxstyle='square,pad=0.08', facecolor='white',
                edgecolor='none', alpha=1.0)


def _save(fig, name):
    path = os.path.join(OUTPUT_DIR, name)
    fig.savefig(path, bbox_inches='tight', dpi=300,
                facecolor='white', edgecolor='none')
    print(f"  -> {path}")
    plt.close(fig)


# ============================================================
# 图 4.1  B公司研发组织架构演变
# ============================================================
def create_org_evolution():
    W = DISPLAY_W
    H = W * 0.65
    fig, axes = plt.subplots(1, 2, figsize=(W, H))

    # 左图: 烟囱式架构
    ax1 = axes[0]
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title('(a) 调整前：烟囱式架构', fontsize=FS, fontweight='bold', pad=8)

    departments = ['语音', '图像', '文本', '知识\n图谱', 'NLP', '推荐', '广告', '搜索']
    hatches = ['//', '\\\\', '..', 'xx', '++', '||', '--', 'oo']

    for i, (dept, h) in enumerate(zip(departments, hatches)):
        x = 1 + (i % 4) * 2.2
        y = 6.8 - (i // 4) * 3.2
        rect = FancyBboxPatch((x - 0.85, y - 0.75), 1.7, 1.5,
                              boxstyle='round,pad=0.06',
                              facecolor='white', edgecolor='black',
                              linewidth=0.8, hatch=h, zorder=1)
        ax1.add_patch(rect)
        ax1.text(x, y, dept, ha='center', va='center', fontsize=FS,
                 fontweight='bold', bbox=_tbg(), zorder=2)

    # 问题标注
    ax1.text(5, 9.2, '沟通壁垒 / 部门墙', ha='center', fontsize=FS,
             fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.15', facecolor='white',
                       edgecolor='black', linewidth=0.8))

    # 纵向虚线分隔各部门
    for i in range(1, 4):
        x = (i % 4) * 2.2 + 0.1
        ax1.plot([x, x], [2.5, 8.2], color='black', lw=0.4, ls=':', alpha=0.4)

    # 右图: BMU/AMU架构
    ax2 = axes[1]
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title('(b) 调整后：BMU/AMU双BU架构', fontsize=FS, fontweight='bold', pad=8)

    # BMU
    bmu = FancyBboxPatch((0.3, 5.2), 4.2, 3.2, boxstyle='round,pad=0.1',
                         facecolor='white', edgecolor='black',
                         linewidth=1.2, hatch='//', zorder=1)
    ax2.add_patch(bmu)
    ax2.text(2.4, 7.5, 'BMU', ha='center', va='center', fontsize=FS,
             fontweight='bold', bbox=_tbg(), zorder=2)
    ax2.text(2.4, 6.5, '基础模型\n与理解', ha='center', va='center', fontsize=FS,
             bbox=_tbg(), zorder=2)
    ax2.text(2.4, 5.6, '(平台团队)', ha='center', va='center',
             fontsize=FS_SMALL, style='italic', bbox=_tbg(), zorder=2)

    # AMU
    amu = FancyBboxPatch((5.5, 5.2), 4.2, 3.2, boxstyle='round,pad=0.1',
                         facecolor='white', edgecolor='black',
                         linewidth=1.2, hatch='\\\\', zorder=1)
    ax2.add_patch(amu)
    ax2.text(7.6, 7.5, 'AMU', ha='center', va='center', fontsize=FS,
             fontweight='bold', bbox=_tbg(), zorder=2)
    ax2.text(7.6, 6.5, '应用与\n多模态', ha='center', va='center', fontsize=FS,
             bbox=_tbg(), zorder=2)
    ax2.text(7.6, 5.6, '(流对齐团队)', ha='center', va='center',
             fontsize=FS_SMALL, style='italic', bbox=_tbg(), zorder=2)

    # 共性平台层
    platform = FancyBboxPatch((1.2, 2.6), 7.6, 1.6, boxstyle='round,pad=0.08',
                              facecolor='white', edgecolor='black',
                              linewidth=1.2, hatch='..', zorder=1)
    ax2.add_patch(platform)
    ax2.text(5, 3.4, '共性平台层', ha='center', va='center',
             fontsize=FS, fontweight='bold', bbox=_tbg(), zorder=2)

    # 业务场景
    scenarios = ['搜索', '智能云', 'Apollo', '智能设备']
    for i, sc in enumerate(scenarios):
        x = 1.8 + i * 2.0
        rect = FancyBboxPatch((x - 0.75, 0.5), 1.5, 1.2,
                              boxstyle='round,pad=0.06',
                              facecolor='white', edgecolor='black',
                              linewidth=0.8, hatch='xx', zorder=1)
        ax2.add_patch(rect)
        ax2.text(x, 1.1, sc, ha='center', va='center', fontsize=FS,
                 fontweight='bold', bbox=_tbg(), zorder=2)

    # 双向箭头（平台 <-> BU）
    akw = dict(arrowstyle='<->', lw=1.0, color='black')
    ax2.annotate('', xy=(5, 5.2), xytext=(5, 4.2), arrowprops=akw)

    # 协同标签
    ax2.text(5, 9.2, '统一规划 / 协同高效', ha='center', fontsize=FS,
             fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.15', facecolor='white',
                       edgecolor='black', linewidth=0.8))

    fig.tight_layout()
    _save(fig, 'baidu-org-evolution.pdf')


# ============================================================
# 图 4.2  SWOT战略四象限雷达图
# ============================================================
def create_swot_radar():
    W = DISPLAY_W
    H = W * 0.72
    fig, ax = plt.subplots(figsize=(W, H), subplot_kw=dict(projection='polar'))

    categories = ['SO\n优势-机会', 'WO\n劣势-机会',
                  'WT\n劣势-威胁', 'ST\n优势-威胁']
    N = len(categories)

    baidu_scores = [4.15, 3.85, 2.10, 2.40]
    industry_avg = [3.50, 3.20, 2.80, 2.60]
    benchmark = [4.30, 3.60, 2.40, 2.80]

    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]

    baidu_scores += baidu_scores[:1]
    industry_avg += industry_avg[:1]
    benchmark += benchmark[:1]

    # B公司 —— 实线圆点
    ax.plot(angles, baidu_scores, 'o-', linewidth=1.5, label='B公司',
            color='black', markersize=5, markerfacecolor='white',
            markeredgecolor='black', markeredgewidth=1.0)

    # 行业平均 —— 虚线方点
    ax.plot(angles, industry_avg, 's--', linewidth=1.2, label='行业平均',
            color='black', markersize=5, markerfacecolor='gray',
            markeredgecolor='black', markeredgewidth=0.8)

    # 标杆企业 —— 点划线三角
    ax.plot(angles, benchmark, '^-.', linewidth=1.2, label='标杆企业',
            color='black', markersize=5, markerfacecolor='black',
            markeredgecolor='black', markeredgewidth=0.8)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=FS_SMALL)
    ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.tick_params(axis='y', labelsize=6)
    ax.grid(True, linestyle='--', alpha=0.5, linewidth=0.5)

    ax.legend(loc='upper right', bbox_to_anchor=(1.35, 1.1),
              fontsize=FS_SMALL, frameon=True, edgecolor='black',
              fancybox=False)

    fig.tight_layout()
    _save(fig, 'swot-radar-baidu.pdf')


# ============================================================
# 图 4.3  AMO三维对比（热力图 → B&W 分组柱状图）
# ============================================================
def create_amo_comparison():
    W = DISPLAY_W
    H = W * 0.50
    fig, ax = plt.subplots(figsize=(W, H))

    companies = ['B公司', '阿里巴巴', '腾讯', '字节跳动', '行业平均']
    dimensions = ['能力(A)', '动机(M)', '机会(O)']
    data = np.array([
        [3.8, 3.2, 3.5],
        [4.0, 3.8, 3.8],
        [3.9, 3.6, 3.7],
        [4.2, 4.0, 4.1],
        [3.5, 3.4, 3.5],
    ])

    x = np.arange(len(companies))
    width = 0.22
    hatches = ['//', '\\\\', '..']

    for i, (dim, h) in enumerate(zip(dimensions, hatches)):
        bars = ax.bar(x + i * width - width, data[:, i], width,
                      facecolor='white', edgecolor='black', linewidth=0.8,
                      hatch=h, label=dim)
        for bar in bars:
            ht = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, ht + 0.05,
                    f'{ht:.1f}', ha='center', va='bottom', fontsize=8)

    ax.set_xticks(x)
    ax.set_xticklabels(companies, fontsize=FS_SMALL)
    ax.set_ylabel('得分（1-5分）', fontsize=FS)
    ax.tick_params(axis='y', labelsize=FS_TICK)
    ax.set_ylim(0, 5)
    ax.legend(fontsize=FS_SMALL, frameon=True, edgecolor='black',
              fancybox=False, loc='upper right')
    ax.grid(True, alpha=0.3, axis='y', linestyle='--', linewidth=0.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.tight_layout()
    _save(fig, 'amo-comparison.pdf')


# ============================================================
# Main
# ============================================================
def main():
    print("=" * 60)
    print("生成第四章图表（黑白打印版）")
    print("=" * 60)
    create_org_evolution()
    create_swot_radar()
    create_amo_comparison()
    print("=" * 60)
    print("完成！共3张图。")


if __name__ == '__main__':
    main()
