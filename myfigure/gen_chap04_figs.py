#!/usr/bin/env python3
"""生成第4章所有缺失图片"""
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
# 1. SWOT雷达图
# ─────────────────────────────────────────────
def gen_swot_radar():
    categories = ['优势(S)\n技术积累', '机会(O)\n政策+大模型', '劣势(W)\n组织复杂度', '威胁(T)\n竞争+芯片']
    N = len(categories)
    baidu     = [4.15, 4.05, 2.75, 3.0]
    benchmark = [3.5,  4.2,  3.2,  3.1]
    angles = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
    angles += angles[:1]
    baidu     += baidu[:1]
    benchmark += benchmark[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.plot(angles, baidu,     'o-',  lw=2,   color='#2563EB', label='百度')
    ax.fill(angles, baidu,    alpha=0.15, color='#2563EB')
    ax.plot(angles, benchmark, 's--', lw=1.5, color='#DC2626', label='行业均值')
    ax.fill(angles, benchmark, alpha=0.08, color='#DC2626')
    ax.set_thetagrids(np.degrees(angles[:-1]), categories)
    ax.set_ylim(0, 5)
    ax.set_yticks([1,2,3,4,5])
    ax.set_yticklabels(['1','2','3','4','5'], fontsize=8)
    ax.set_title('百度研发管理SWOT战略雷达图', pad=20, fontsize=13, fontweight='bold')
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    plt.tight_layout()
    for ext in ('pdf', 'png'):
        plt.savefig(os.path.join(OUT, f'swot-radar-baidu.{ext}'), dpi=150, bbox_inches='tight')
    plt.close()
    print("swot-radar-baidu done")

# ─────────────────────────────────────────────
# 2. AMO三维对比柱状图
# ─────────────────────────────────────────────
def gen_amo_comparison():
    dims      = ['能力(A)', '动机(M)', '机会(O)']
    companies = ['百度', '字节跳动', '阿里巴巴', '腾讯']
    data = [
        [3.8, 3.2, 3.5],
        [4.0, 4.2, 4.1],
        [3.9, 3.8, 3.9],
        [3.7, 3.6, 3.8],
    ]
    colors = ['#2563EB', '#DC2626', '#16A34A', '#D97706']
    x = np.arange(len(dims))
    width = 0.18
    fig, ax = plt.subplots(figsize=(8, 5))
    for i, (company, scores, color) in enumerate(zip(companies, data, colors)):
        offset = (i - 1.5) * width
        ax.bar(x + offset, scores, width, label=company, color=color, alpha=0.85)
    ax.set_xticks(x)
    ax.set_xticklabels(dims, fontsize=12)
    ax.set_ylim(0, 5.2)
    ax.set_ylabel('得分（满分5分）', fontsize=11)
    ax.set_title('百度与行业标杆企业AMO三维度对比', fontsize=13, fontweight='bold', pad=12)
    ax.axhline(y=3.5, color='gray', linestyle='--', lw=1, alpha=0.6, label='行业基准线(3.5)')
    ax.legend(loc='lower right', fontsize=10)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    for ext in ('pdf', 'png'):
        plt.savefig(os.path.join(OUT, f'amo-comparison.{ext}'), dpi=150, bbox_inches='tight')
    plt.close()
    print("amo-comparison done")

# ─────────────────────────────────────────────
# 3. 双通道职业发展路径图
# ─────────────────────────────────────────────
def gen_dual_career():
    fig, ax = plt.subplots(figsize=(9, 6.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title('技术专家双通道职业发展路径', fontsize=14, fontweight='bold', pad=12)

    mgmt_levels = ['P6 高级工程师', 'P7 技术专家', 'P8 高级技术专家', 'P9 总监', 'P10 副总裁']
    tech_levels = ['P6 高级工程师', 'T7 资深技术专家', 'T8 技术委员会成员', 'T9 首席科学家', 'T10 院士级专家']
    mgmt_x, tech_x = 2.5, 7.5

    for i, (ml, tl) in enumerate(zip(mgmt_levels, tech_levels)):
        y = 1.5 + i * 1.4
        # 管理通道
        box_m = mpatches.FancyBboxPatch((mgmt_x-1.1, y-0.35), 2.2, 0.7,
            boxstyle="round,pad=0.08", facecolor='#DBEAFE', edgecolor='#2563EB', lw=1.5)
        ax.add_patch(box_m)
        ax.text(mgmt_x, y, ml, ha='center', va='center', fontsize=8.5)
        # 技术通道
        box_t = mpatches.FancyBboxPatch((tech_x-1.1, y-0.35), 2.2, 0.7,
            boxstyle="round,pad=0.08", facecolor='#DCFCE7', edgecolor='#16A34A', lw=1.5)
        ax.add_patch(box_t)
        ax.text(tech_x, y, tl, ha='center', va='center', fontsize=8.5)
        # 向上箭头
        if i < len(mgmt_levels)-1:
            for cx in (mgmt_x, tech_x):
                ax.annotate('', xy=(cx, y+0.45), xytext=(cx, y+0.95),
                           arrowprops=dict(arrowstyle='->', lw=1.5,
                               color='#2563EB' if cx==mgmt_x else '#16A34A'))
        # 横向虚线
        ax.annotate('', xy=(tech_x-1.15, y), xytext=(mgmt_x+1.15, y),
                   arrowprops=dict(arrowstyle='<->', lw=1.0,
                       color='#9CA3AF', linestyle='dashed'))

    ax.text(mgmt_x, 0.8, '管理发展通道', ha='center', fontsize=11, fontweight='bold', color='#2563EB')
    ax.text(tech_x, 0.8, '技术专家通道', ha='center', fontsize=11, fontweight='bold', color='#16A34A')
    ax.text(5.0, 0.4, '← 两通道支持横向转换 →', ha='center', fontsize=9, color='#6B7280', style='italic')
    plt.tight_layout()
    for ext in ('pdf', 'png'):
        plt.savefig(os.path.join(OUT, f'dual-career-channel.{ext}'), dpi=150, bbox_inches='tight')
    plt.close()
    print("dual-career-channel done")

# ─────────────────────────────────────────────
# 4. 研发效能多维看板（雷达图）
# ─────────────────────────────────────────────
def gen_rd_dashboard():
    categories = ['技术资产\n周转率', 'DORA\n研发效率', '人才\n留存率', '创新\n产出', '技术债务\n控制', '跨团队\n协作']
    N = len(categories)
    # 5分制
    current = [1.12, 2.5, 2.8, 3.0, 2.0, 2.5]
    target  = [2.5,  4.0, 4.0, 4.2, 3.5, 4.0]
    angles = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
    angles += angles[:1]
    c = current + current[:1]
    t = target  + target[:1]

    fig, ax = plt.subplots(figsize=(6.5, 6.5), subplot_kw=dict(polar=True))
    ax.plot(angles, c, 'o-', lw=2,   color='#DC2626', label='当前状态')
    ax.fill(angles, c, alpha=0.15,  color='#DC2626')
    ax.plot(angles, t, 's-', lw=2,   color='#16A34A', label='改进目标')
    ax.fill(angles, t, alpha=0.12,  color='#16A34A')
    ax.set_thetagrids(np.degrees(angles[:-1]), categories, fontsize=10)
    ax.set_ylim(0, 5)
    ax.set_yticks([1,2,3,4,5])
    ax.set_yticklabels(['1','2','3','4','5'], fontsize=8)
    ax.set_title('百度研发效能多维度看板\n（当前状态 vs 改进目标）', pad=20, fontsize=12, fontweight='bold')
    ax.legend(loc='upper right', bbox_to_anchor=(1.35, 1.1))
    plt.tight_layout()
    for ext in ('pdf', 'png'):
        plt.savefig(os.path.join(OUT, f'rd-effectiveness-dashboard.{ext}'), dpi=150, bbox_inches='tight')
    plt.close()
    print("rd-effectiveness-dashboard done")

# ─────────────────────────────────────────────
# 5. PDCA持续改进循环
# ─────────────────────────────────────────────
def gen_pdca():
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_xlim(-1.8, 1.8)
    ax.set_ylim(-1.8, 1.8)
    ax.axis('off')
    ax.set_aspect('equal')

    colors  = ['#2563EB', '#16A34A', '#D97706', '#DC2626']
    labels  = ['P\nPlan\n计划', 'D\nDo\n执行', 'C\nCheck\n检查', 'A\nAct\n改进']
    subs    = ['设定研发效能\n目标与指标', '实施管理\n改进措施', '评估技术资产\n周转率变化', '固化最佳实践\n推进下一循环']
    angles_center = [90, 0, 270, 180]  # 各象限中心角

    for color, label, sub, ac in zip(colors, labels, subs, angles_center):
        wedge = mpatches.Wedge((0,0), 1.2, ac-45, ac+45,
                               facecolor=color, alpha=0.78, edgecolor='white', lw=3)
        ax.add_patch(wedge)
        rad = np.radians(ac)
        tx, ty = 0.65*np.cos(rad), 0.65*np.sin(rad)
        ax.text(tx, ty, label, ha='center', va='center', fontsize=11,
                fontweight='bold', color='white')
        sx, sy = 1.52*np.cos(rad), 1.52*np.sin(rad)
        ax.text(sx, sy, sub, ha='center', va='center', fontsize=9, color='#374151')

    # 中心白圆
    center = plt.Circle((0,0), 0.3, color='white', zorder=5)
    ax.add_patch(center)
    ax.text(0, 0, 'PDCA\n持续改进', ha='center', va='center',
            fontsize=10, fontweight='bold', color='#1E3A5F', zorder=6)

    # 顺时针箭头环
    arrow_angles = [67.5, 337.5, 247.5, 157.5]
    for aa in arrow_angles:
        rad = np.radians(aa)
        px, py = 1.28*np.cos(rad), 1.28*np.sin(rad)
        dx, dy = -0.01*np.sin(rad), 0.01*np.cos(rad)
        ax.annotate('', xy=(px+dx*8, py+dy*8), xytext=(px, py),
                   arrowprops=dict(arrowstyle='->', color='#6B7280', lw=1.5))

    ax.set_title('百度研发管理PDCA持续改进循环', fontsize=13, fontweight='bold', y=1.02)
    plt.tight_layout()
    for ext in ('pdf', 'png'):
        plt.savefig(os.path.join(OUT, f'pdca-improvement.{ext}'), dpi=150, bbox_inches='tight')
    plt.close()
    print("pdca-improvement done")

if __name__ == '__main__':
    gen_swot_radar()
    gen_amo_comparison()
    gen_dual_career()
    gen_rd_dashboard()
    gen_pdca()
    print("All done.")
