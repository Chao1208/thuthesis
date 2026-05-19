#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成第三章所有图表（黑白打印版）
- 10pt 宋体 / Times New Roman（figsize=显示宽度，不缩放）
- 8pt 坐标轴刻度
- 纹理区分模块
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.patches import FancyBboxPatch
import numpy as np
import os

# thuthesis: A4, margin=3cm → textwidth=150mm=5.91in
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

FS = 10       # 正文/标签字号
FS_TICK = 8   # 刻度字号
FS_SMALL = 8  # 小字（数据标注等）

# 纹理列表，用于区分不同系列
HATCHES = ['//', '\\\\', '..', 'xx', '++', '||', '--', 'oo']
# 标记列表，用于区分不同折线
MARKERS = ['o', 's', '^', 'D', 'v', 'p', 'h']


def _save(fig, name):
    path = os.path.join(OUTPUT_DIR, name)
    fig.savefig(path, bbox_inches='tight', dpi=300,
                facecolor='white', edgecolor='none')
    print(f"  -> {path}")
    plt.close(fig)


# ============================================================
# 图 3.1  中国互联网网民规模与企业数量增长趋势（2000-2010）
# ============================================================
def create_internet_development():
    W = DISPLAY_W
    H = W * 0.62
    fig, ax1 = plt.subplots(figsize=(W, H))

    years = np.array([2000, 2002, 2004, 2006, 2008, 2010])
    netizens = np.array([0.23, 0.59, 0.94, 1.37, 2.98, 4.57])
    companies = np.array([1000, 2500, 5000, 9500, 15000, 20000])

    # 网民规模（左轴）—— 实线圆点
    ax1.plot(years, netizens, color='black', linewidth=1.5, marker='o',
             markersize=5, markerfacecolor='white', markeredgecolor='black',
             markeredgewidth=1.0, label='网民规模', zorder=3)
    ax1.set_xlabel('年份', fontsize=FS)
    ax1.set_ylabel('网民规模（亿人）', fontsize=FS)
    ax1.tick_params(axis='both', labelsize=FS_TICK)
    ax1.set_ylim(0, 5.5)
    ax1.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)

    for x, y in zip(years, netizens):
        ax1.text(x, y - 0.15, f'{y:.2f}', ha='center', va='top',
                 fontsize=FS_SMALL, color='black')

    # 企业数量（右轴）—— 虚线方点
    ax2 = ax1.twinx()
    ax2.plot(years, companies, color='black', linewidth=1.5, marker='s',
             markersize=5, markerfacecolor='black', markeredgecolor='black',
             markeredgewidth=1.0, linestyle='--', label='企业数量', zorder=3)
    ax2.set_ylabel('互联网企业数量（家）', fontsize=FS)
    ax2.tick_params(axis='y', labelsize=FS_TICK)
    ax2.set_ylim(0, 24000)

    for x, y in zip(years, companies):
        ax2.text(x, y + 600, f'{y:,}', ha='center', va='bottom',
                 fontsize=FS_SMALL, color='black')

    # 合并图例
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left',
               fontsize=FS_SMALL, frameon=True, edgecolor='black',
               fancybox=False)

    fig.tight_layout()
    _save(fig, 'internet-development-2000-2010.pdf')


# ============================================================
# 图 3.2  中国互联网百强企业研发投入增长趋势（2010-2020）
# ============================================================
def create_rnd_investment_growth():
    W = DISPLAY_W
    H = W * 0.60
    fig, ax1 = plt.subplots(figsize=(W, H))

    years = np.array([2010, 2012, 2014, 2016, 2018, 2020])
    investment = np.array([380, 620, 890, 1150, 1560, 1898])
    growth_rate = np.array([28, 35, 25, 22, 27, 21])

    # 柱状图 —— 斜纹
    bars = ax1.bar(years, investment, width=1.2, facecolor='white',
                   edgecolor='black', linewidth=1.0, hatch='//',
                   label='研发投入', zorder=2)
    ax1.set_xlabel('年份', fontsize=FS)
    ax1.set_ylabel('研发投入（亿元）', fontsize=FS)
    ax1.tick_params(axis='both', labelsize=FS_TICK)
    ax1.set_ylim(0, 2400)
    ax1.grid(True, alpha=0.3, linestyle='--', linewidth=0.5, axis='y')

    for bar in bars:
        h = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, h + 40,
                 f'{int(h)}', ha='center', va='bottom',
                 fontsize=FS_SMALL)

    # 增长率折线（右轴）
    ax2 = ax1.twinx()
    ax2.plot(years, growth_rate, color='black', linewidth=1.5,
             marker='D', markersize=5, markerfacecolor='black',
             markeredgecolor='black', label='增长率', zorder=3)
    ax2.set_ylabel('同比增长率（%）', fontsize=FS)
    ax2.tick_params(axis='y', labelsize=FS_TICK)
    ax2.set_ylim(0, 45)

    for x, y in zip(years, growth_rate):
        ax2.text(x, y + 1.5, f'{y}%', ha='center', va='bottom',
                 fontsize=FS_SMALL)

    # 合并图例
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left',
               fontsize=FS_SMALL, frameon=True, edgecolor='black',
               fancybox=False)

    fig.tight_layout()
    _save(fig, 'rnd-investment-growth.pdf')


# ============================================================
# 图 3.3  敏捷开发与DevOps方法应用率变化（2010-2023）
# ============================================================
def create_agile_adoption_rate():
    W = DISPLAY_W
    H = W * 0.58
    fig, ax = plt.subplots(figsize=(W, H))

    years = np.array([2010, 2012, 2014, 2016, 2018, 2020, 2022, 2023])
    agile_rate = np.array([15, 22, 35, 52, 68, 78, 80, 82])
    devops_rate = np.array([5, 10, 18, 28, 45, 65, 70, 72])

    # 实线圆点 —— 敏捷
    ax.plot(years, agile_rate, color='black', linewidth=1.5, marker='o',
            markersize=5, markerfacecolor='white', markeredgecolor='black',
            markeredgewidth=1.0, label='敏捷开发应用率')
    # 虚线方点 —— DevOps
    ax.plot(years, devops_rate, color='black', linewidth=1.5, marker='s',
            markersize=5, markerfacecolor='black', markeredgecolor='black',
            markeredgewidth=1.0, linestyle='--', label='DevOps应用率')

    # 标注关键年份
    for i in [0, 3, 7]:
        ax.annotate(f'{agile_rate[i]}%', xy=(years[i], agile_rate[i]),
                    xytext=(0, 8), textcoords='offset points',
                    ha='center', fontsize=FS_SMALL)
        ax.annotate(f'{devops_rate[i]}%', xy=(years[i], devops_rate[i]),
                    xytext=(0, -12), textcoords='offset points',
                    ha='center', fontsize=FS_SMALL)

    ax.set_xlabel('年份', fontsize=FS)
    ax.set_ylabel('应用率（%）', fontsize=FS)
    ax.tick_params(axis='both', labelsize=FS_TICK)
    ax.set_ylim(0, 95)
    ax.set_xticks(years)
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
    ax.legend(fontsize=FS_SMALL, loc='upper left', frameon=True,
              edgecolor='black', fancybox=False)

    fig.tight_layout()
    _save(fig, 'agile-adoption-rate.pdf')


# ============================================================
# 图 3.4  DevOps实践前后关键指标对比
# ============================================================
def create_devops_metrics_comparison():
    W = DISPLAY_W
    H = W * 0.55
    fig, axes = plt.subplots(1, 2, figsize=(W, H),
                             gridspec_kw={'width_ratios': [1.3, 1]})

    # 左图：绝对值对比（分组柱状图）
    metrics = ['部署频率\n(次/月)', '交付周期\n(天)', '故障恢复\n(小时)',
               '变更失败率\n(%)', '自动化率\n(%)']
    traditional = [1.5, 37.5, 6.0, 17.5, 40]
    devops = [30, 10.5, 1.25, 6.5, 85]

    x = np.arange(len(metrics))
    width = 0.32

    ax = axes[0]
    b1 = ax.bar(x - width / 2, traditional, width, facecolor='white',
                edgecolor='black', linewidth=0.8, hatch='//', label='传统模式')
    b2 = ax.bar(x + width / 2, devops, width, facecolor='white',
                edgecolor='black', linewidth=0.8, hatch='..', label='DevOps模式')
    ax.set_xticks(x)
    ax.set_xticklabels(metrics, fontsize=FS_TICK)
    ax.tick_params(axis='y', labelsize=FS_TICK)
    ax.set_ylabel('原始数值', fontsize=FS_SMALL)
    ax.legend(fontsize=FS_TICK, frameon=True, edgecolor='black', fancybox=False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    for bar in b1:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, h + 0.5,
                f'{h:g}', ha='center', va='bottom', fontsize=FS_TICK)
    for bar in b2:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, h + 0.5,
                f'{h:g}', ha='center', va='bottom', fontsize=FS_TICK)

    # 右图：改善幅度（水平柱状图）
    ax2 = axes[1]
    improvements = ['部署频率\n提升20倍', '交付周期\n缩短72%',
                    '故障恢复\n缩短79%', '变更失败率\n降低63%',
                    '自动化率\n提升113%']
    imp_values = [20, 72, 79, 63, 113]
    hatches_imp = ['//', '\\\\', '..', 'xx', '++']

    bars2 = ax2.barh(improvements, imp_values, facecolor='white',
                     edgecolor='black', linewidth=0.8)
    for bar, h in zip(bars2, hatches_imp):
        bar.set_hatch(h)

    for bar, val in zip(bars2, imp_values):
        label = f'{val}×' if val == 20 else f'{val}%'
        ax2.text(val + 1.5, bar.get_y() + bar.get_height() / 2,
                 label, va='center', fontsize=FS_TICK, fontweight='bold')

    ax2.tick_params(axis='both', labelsize=FS_TICK)
    ax2.set_xlabel('改善幅度', fontsize=FS_SMALL)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)

    fig.tight_layout()
    _save(fig, 'devops-metrics-comparison.pdf')


# ============================================================
# 图 3.5  互联网企业创新激励机制构成（2023）
# ============================================================
def create_innovation_incentive_system():
    W = DISPLAY_W
    H = W * 0.78
    fig, axes = plt.subplots(2, 2, figsize=(W, H))

    categories = ['物质激励', '精神激励', '发展激励', '环境激励']
    subcategories = [
        [('薪酬奖金', 68), ('股权激励', 58), ('项目奖金', 62)],
        [('技术表彰', 72), ('技术分享', 85), ('技术竞赛', 48)],
        [('技术晋升', 92), ('培训机会', 78), ('轮岗机制', 35)],
        [('创新时间', 35), ('创新基金', 52), ('孵化支持', 28)],
    ]
    sub_hatches = [['//', '\\\\', '..'],
                   ['xx', '++', '||'],
                   ['//', '\\\\', '..'],
                   ['xx', '++', '||']]

    for idx, (ax, cat, subs, hs) in enumerate(
            zip(axes.flatten(), categories, subcategories, sub_hatches)):
        labels = [s[0] for s in subs]
        values = [s[1] for s in subs]

        bars = ax.barh(labels, values, facecolor='white', edgecolor='black',
                       linewidth=0.8)
        for bar, h in zip(bars, hs):
            bar.set_hatch(h)

        for bar in bars:
            w = bar.get_width()
            ax.text(w + 1.5, bar.get_y() + bar.get_height() / 2,
                    f'{int(w)}%', ha='left', va='center', fontsize=FS_SMALL)

        ax.set_xlabel('应用率（%）', fontsize=FS_SMALL)
        ax.set_title(cat, fontsize=FS, fontweight='bold', pad=6)
        ax.set_xlim(0, 100)
        ax.grid(True, alpha=0.3, axis='x', linestyle='--', linewidth=0.5)
        ax.tick_params(labelsize=FS_TICK)

    fig.tight_layout()
    _save(fig, 'innovation-incentive-system.pdf')


# ============================================================
# 图 3.6  主要互联网上市公司技术资产周转率（2019-2024）
# ============================================================
def create_rd_capital_turnover():
    W = DISPLAY_W
    H = W * 0.65

    DELTA = 0.15
    G0 = 0.10
    YEARS = np.array([2019, 2020, 2021, 2022, 2023, 2024])

    RD = {
        'B公司':    np.array([185.8, 199.0, 222.0, 233.0, 242.2, 219.3]),
        '阿里巴巴': np.array([300.9, 360.0, 445.0, 429.0, 382.0, 588.0]),
        '京东':     np.array([117.0, 149.3, 163.0, 170.0, 169.0, 168.0]),
        '拼多多':   np.array([39.0,  60.0,  89.0,  104.0, 110.0, 147.0]),
        '网易':     np.array([70.0,  84.0,  104.0, 141.0, 150.0, 156.0]),
        '哔哩哔哩': np.array([14.0,  21.0,  38.0,  48.0,  45.0,  47.0]),
        '携程':     np.array([90.0,  77.0,  83.0,  83.0,  121.0, 98.0]),
    }
    REV = {
        'B公司':    np.array([1074.0, 1072.0, 1245.0, 1237.0, 1346.0, 1343.0]),
        '阿里巴巴': np.array([3768.0, 5097.0, 7173.0, 8687.0, 9411.0, 9880.0]),
        '京东':     np.array([5769.0, 7458.0, 9516.0, 10462.0, 10847.0, 11455.0]),
        '拼多多':   np.array([301.0,  595.0,  1397.0, 1306.0, 2476.0, 3940.0]),
        '网易':     np.array([552.0,  618.0,  732.0,  931.0,  993.0,  970.0]),
        '哔哩哔哩': np.array([67.0,   120.0,  194.0,  219.0,  225.0,  269.0]),
        '携程':     np.array([357.0,  183.0,  196.0,  356.0,  765.0,  862.0]),
    }

    def calc_turnover(rd, rev):
        n = len(rd)
        K = np.zeros(n)
        K_init = rd[0] / (G0 + DELTA)
        K[0] = (1 - DELTA) * K_init + rd[0]
        for t in range(1, n):
            K[t] = (1 - DELTA) * K[t - 1] + rd[t]
        return rev / K

    COMPANIES = list(RD.keys())
    TURNOVER = {}
    for c in COMPANIES:
        TURNOVER[c] = calc_turnover(RD[c], REV[c])

    fig, ax = plt.subplots(figsize=(W, H))

    # 用不同标记和线型区分7家公司
    line_styles = ['-', '--', '-.', ':', '-', '--', '-.']
    for i, company in enumerate(COMPANIES):
        mk = MARKERS[i]
        ls = line_styles[i]
        lw = 2.0 if company == 'B公司' else 1.2
        zorder = 10 if company == 'B公司' else 5
        ax.plot(YEARS, TURNOVER[company], color='black',
                marker=mk, markersize=4.5, linewidth=lw,
                linestyle=ls, label=company, zorder=zorder,
                markerfacecolor='white' if i % 2 == 0 else 'black',
                markeredgecolor='black', markeredgewidth=0.8)

    # B公司端点标注
    bd = TURNOVER['B公司']
    ax.annotate(f'{bd[0]:.2f}', xy=(YEARS[0], bd[0]),
                xytext=(-20, 5), textcoords='offset points',
                fontsize=9, fontweight='bold')
    ax.annotate(f'{bd[-1]:.2f}', xy=(YEARS[-1], bd[-1]),
                xytext=(4, -10), textcoords='offset points',
                fontsize=9, fontweight='bold')

    ax.set_xlabel('年份', fontsize=FS)
    ax.set_ylabel('技术资产周转率（倍）', fontsize=FS)
    ax.set_xticks(YEARS)
    ax.set_xticklabels([str(y) for y in YEARS], fontsize=8)
    ax.tick_params(axis='y', labelsize=8)
    ax.set_xlim(2018.5, 2024.5)
    ax.set_ylim(0, 20)
    ax.yaxis.set_major_locator(ticker.MultipleLocator(2))
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
    ax.legend(loc='upper left', ncol=2, fontsize=9,
              frameon=True, edgecolor='black', fancybox=False)

    fig.tight_layout()
    _save(fig, 'rd-capital-turnover.pdf')


# ============================================================
# 图 3.7  头部互联网企业AI研发投入及增速（2024年）
# ============================================================
def create_ai_rd_investment():
    W = DISPLAY_W
    H = W * 0.55
    fig, ax = plt.subplots(figsize=(W, H))

    companies = ['阿里巴巴', '腾讯', 'B公司', '京东', '网易', '拼多多', '哔哩哔哩']
    rd_amount = [588, 707, 219, 163, 156, 147, 47]
    growth = [53.9, 10.3, -9.5, -0.6, -5.5, 33.6, 4.4]

    y_pos = np.arange(len(companies))
    # 按研发费用排序（已手动排好：腾讯>阿里>百度>京东>网易>拼多多>B站）
    # 重新排序：从大到小
    order = np.argsort(rd_amount)[::-1]
    companies = [companies[i] for i in order]
    rd_amount = [rd_amount[i] for i in order]
    growth = [growth[i] for i in order]

    bars = ax.barh(y_pos, rd_amount, facecolor='white', edgecolor='black',
                   linewidth=0.8)
    # 为正增长和负增长使用不同纹理
    for bar, g in zip(bars, growth):
        if g >= 0:
            bar.set_hatch('//')
        else:
            bar.set_hatch('xx')

    ax.set_yticks(y_pos)
    ax.set_yticklabels(companies, fontsize=FS_SMALL)
    ax.set_xlabel('研发费用（亿元）', fontsize=FS)
    ax.tick_params(axis='x', labelsize=FS_TICK)
    ax.invert_yaxis()

    # 数值标签
    for bar, val, g in zip(bars, rd_amount, growth):
        sign = '+' if g > 0 else ''
        ax.text(val + 8, bar.get_y() + bar.get_height() / 2,
                f'{val}亿（{sign}{g}%）', va='center',
                fontsize=FS_SMALL)

    # 图例说明纹理
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='white', edgecolor='black', hatch='//', label='正增长'),
        Patch(facecolor='white', edgecolor='black', hatch='xx', label='负增长'),
    ]
    ax.legend(handles=legend_elements, fontsize=FS_SMALL, loc='lower right',
              frameon=True, edgecolor='black', fancybox=False)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(True, alpha=0.3, axis='x', linestyle='--', linewidth=0.5)

    fig.tight_layout()
    _save(fig, 'ai-rd-investment-2024.pdf')


# ============================================================
# 图 3.8  研发管理困境四象限图
# ============================================================
def create_challenges_quadrant():
    W = DISPLAY_W
    H = W * 0.78
    fig, ax = plt.subplots(figsize=(W, H))

    challenges = [
        {'name': '成本压力',  'x': 4.5, 'y': 4.5,
         'detail': '投入增速5.3%\n裁员30万人'},
        {'name': 'AI技术变革', 'x': 4.2, 'y': 4.8,
         'detail': '62%难以跟上\n56%缺乏经验'},
        {'name': '创新困境',  'x': 4.0, 'y': 3.2,
         'detail': '技术债务35-45%\n周期需<30天'},
        {'name': '组织协作',  'x': 3.8, 'y': 3.0,
         'detail': '重复开发30-40%\n复用率15-20%'},
        {'name': '人才流失',  'x': 3.5, 'y': 4.0,
         'detail': '离职率25.3%\n满意度6.2/10'},
        {'name': '远程协作',  'x': 2.8, 'y': 2.5,
         'detail': '52%混合办公\n效率降15-25%'},
    ]

    ax.set_xlim(1.5, 5.5)
    ax.set_ylim(1.5, 5.5)

    # 四象限分隔线
    ax.axvline(x=3.5, color='black', linestyle='--', linewidth=0.8, alpha=0.5)
    ax.axhline(y=3.5, color='black', linestyle='--', linewidth=0.8, alpha=0.5)

    # 象限标签
    ax.text(4.5, 5.3, '高重要·高紧迫', ha='center', fontsize=FS_SMALL,
            style='italic')
    ax.text(2.5, 5.3, '低重要·高紧迫', ha='center', fontsize=FS_SMALL,
            style='italic')
    ax.text(4.5, 1.7, '高重要·低紧迫', ha='center', fontsize=FS_SMALL,
            style='italic')
    ax.text(2.5, 1.7, '低重要·低紧迫', ha='center', fontsize=FS_SMALL,
            style='italic')

    # 绘制气泡（用不同纹理的圆）
    bubble_hatches = ['//', '\\\\', '..', 'xx', '++', '||']
    for i, ch in enumerate(challenges):
        circle = plt.Circle((ch['x'], ch['y']), 0.35,
                            facecolor='white', edgecolor='black',
                            linewidth=1.2, hatch=bubble_hatches[i], zorder=2)
        ax.add_patch(circle)
        # 名称
        ax.text(ch['x'], ch['y'], ch['name'], ha='center', va='center',
                fontsize=FS_SMALL, fontweight='bold',
                bbox=dict(boxstyle='square,pad=0.05', facecolor='white',
                          edgecolor='none', alpha=0.9),
                zorder=3)
        # 详情标注（偏移到圆外）
        offset_x = 0.55 if ch['x'] >= 3.5 else -0.55
        offset_y = 0.45 if ch['y'] >= 3.5 else -0.45
        tx = ch['x'] + offset_x
        ty = ch['y'] + offset_y
        # 确保不超出范围
        tx = max(1.8, min(5.2, tx))
        ty = max(1.8, min(5.2, ty))
        ax.annotate(ch['detail'],
                    xy=(ch['x'], ch['y']),
                    xytext=(tx, ty),
                    fontsize=6, ha='center', va='center',
                    bbox=dict(boxstyle='round,pad=0.15', facecolor='white',
                              edgecolor='black', linewidth=0.5),
                    arrowprops=dict(arrowstyle='->', color='black',
                                   lw=0.6))

    ax.set_xlabel('重要性', fontsize=FS)
    ax.set_ylabel('紧迫性', fontsize=FS)
    ax.tick_params(axis='both', labelsize=FS_TICK)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.2, linestyle=':', linewidth=0.5)

    fig.tight_layout()
    _save(fig, 'challenges-quadrant.pdf')


# ============================================================
# Main
# ============================================================
def main():
    print("=" * 60)
    print("生成第三章图表（黑白打印版）")
    print("=" * 60)
    create_internet_development()
    create_rnd_investment_growth()
    create_agile_adoption_rate()
    create_devops_metrics_comparison()
    create_innovation_incentive_system()
    create_rd_capital_turnover()
    create_ai_rd_investment()
    create_challenges_quadrant()
    print("=" * 60)
    print("完成！共8张图。")


if __name__ == '__main__':
    main()
