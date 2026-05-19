#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成第二章理论综述的图表（黑白打印版 v5）
- 10pt 宋体 / Times New Roman（figsize=显示宽度，不缩放）
- 纹理区分模块
- 修正标签与主文字重叠问题
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle

# thuthesis: A4, margin=3cm → textwidth=150mm=5.91in
DISPLAY_W = 5.91

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

def _tbg():
    return dict(boxstyle='square,pad=0.1', facecolor='white',
                edgecolor='none', alpha=1.0)

def _lbl():
    return dict(boxstyle='round,pad=0.2', facecolor='white',
                edgecolor='black', linewidth=0.6)

def _save(fig, name):
    fig.savefig(name, bbox_inches='tight', dpi=300,
                facecolor='white', edgecolor='none')
    print(f"  -> {name}")
    plt.close(fig)


# ============================================================
# 图 2.1  AMO 框架
# ============================================================
def create_amo_framework():
    W = DISPLAY_W
    H = W * 0.82
    fig, ax = plt.subplots(figsize=(W, H))
    # 用更宽的坐标范围，给标签留空间
    ax.set_xlim(-1, 11)
    ax.set_ylim(-0.5, 11.5)
    ax.axis('off')

    # 中心圆：员工绩效 —— 斑点
    ax.add_patch(Circle((5, 5), 1.4, facecolor='white', edgecolor='black',
                        linewidth=1.5, hatch='..', zorder=1))
    ax.text(5, 5.35, '员工绩效', ha='center', va='center',
            fontsize=FS, fontweight='bold', bbox=_tbg(), zorder=2)
    ax.text(5, 4.55, 'Performance', ha='center', va='center',
            fontsize=FS, fontfamily='Times New Roman', style='italic',
            bbox=_tbg(), zorder=2)

    # 三要素圆 —— 纹理各不同
    elems = [
        {'xy': (2, 8.2), 'cn': '能力', 'en': 'Ability',    'h': '//'},
        {'xy': (8, 8.2), 'cn': '动机', 'en': 'Motivation',  'h': '\\\\'},
        {'xy': (5, 1.5), 'cn': '机会', 'en': 'Opportunity', 'h': 'xx'},
    ]
    for e in elems:
        ax.add_patch(Circle(e['xy'], 1.1, facecolor='white', edgecolor='black',
                            linewidth=1.5, hatch=e['h'], zorder=1))
        ax.text(e['xy'][0], e['xy'][1] + 0.25, e['cn'], ha='center', va='center',
                fontsize=FS, fontweight='bold', bbox=_tbg(), zorder=2)
        ax.text(e['xy'][0], e['xy'][1] - 0.35, e['en'], ha='center', va='center',
                fontsize=FS, fontfamily='Times New Roman', style='italic',
                bbox=_tbg(), zorder=2)

    # 箭头
    akw = dict(arrowstyle='->', lw=1.2, color='black', mutation_scale=14)
    ax.annotate('', xy=(3.95, 5.95), xytext=(2.85, 7.3), arrowprops=akw)
    ax.annotate('', xy=(6.05, 5.95), xytext=(7.15, 7.3), arrowprops=akw)
    ax.annotate('', xy=(5, 3.7),     xytext=(5, 2.6),     arrowprops=akw)

    # 标签 —— 放在圆的外侧，不与圆内文字重叠
    # 能力标签（左上方，纵向排列，圆上方）
    a_items = ['知识水平', '技能熟练度', '专业能力', '学习能力']
    for i, t in enumerate(a_items):
        ax.text(-0.3, 10.8 - i * 0.55, t, ha='center', va='center',
                fontsize=FS, bbox=_lbl(), zorder=3)

    # 能力标签 → 圆的连线
    ax.plot([-0.3, 2], [9.2, 9.3], color='black', lw=0.6, ls=':', zorder=0)

    # 动机标签（右上方）
    m_items = ['内在动机', '外在激励', '工作热情', '目标导向']
    for i, t in enumerate(m_items):
        ax.text(10.3, 10.8 - i * 0.55, t, ha='center', va='center',
                fontsize=FS, bbox=_lbl(), zorder=3)

    ax.plot([10.3, 8], [9.2, 9.3], color='black', lw=0.6, ls=':', zorder=0)

    # 机会标签（底部横向排列）
    o_items = ['参与决策', '资源支持', '成长机会', '工作自主性']
    for i, t in enumerate(o_items):
        ax.text(1.8 + i * 2.15, -0.2, t, ha='center', va='center',
                fontsize=FS, bbox=_lbl(), zorder=3)

    ax.plot([5, 5], [0.4, 0.15], color='black', lw=0.6, ls=':', zorder=0)

    fig.tight_layout()
    _save(fig, 'amo-framework.pdf')


# ============================================================
# 图 2.2  I-M-O-I 模型
# ============================================================
def create_imoi_model():
    W = DISPLAY_W
    H = W * 0.50  # 给标签更多高度
    fig, ax = plt.subplots(figsize=(W, H))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 7.5)
    ax.axis('off')

    bw, bh = 2.5, 1.8
    by = 2.5  # 框的底部y坐标

    stages = [
        {'x': 0.5,  'cn': '投入',   'en': 'Input',    'h': '//',
         'items': ['组织情境', '团队特征', '个体特征']},
        {'x': 4.0,  'cn': '中介',   'en': 'Mediator', 'h': '\\\\',
         'items': ['团队过程', '涌现状态', '协作机制']},
        {'x': 7.5,  'cn': '产出',   'en': 'Output',   'h': '..',
         'items': ['团队绩效', '成员满意度', '创新产出']},
        {'x': 11.0, 'cn': '再投入', 'en': 'Input',    'h': 'xx',
         'items': ['经验积累', '能力提升', '关系深化']},
    ]

    for s in stages:
        box = FancyBboxPatch((s['x'], by), bw, bh, boxstyle='round,pad=0.1',
                             facecolor='white', edgecolor='black',
                             linewidth=1.5, hatch=s['h'], zorder=1)
        ax.add_patch(box)
        cx = s['x'] + bw / 2
        cy = by + bh / 2
        ax.text(cx, cy + 0.25, s['cn'], ha='center', va='center',
                fontsize=FS, fontweight='bold', bbox=_tbg(), zorder=2)
        ax.text(cx, cy - 0.30, s['en'], ha='center', va='center',
                fontsize=FS, fontfamily='Times New Roman', style='italic',
                bbox=_tbg(), zorder=2)

        # 子项：框上方，间距加大
        for j, item in enumerate(s['items']):
            ax.text(cx, by + bh + 0.35 + j * 0.52, item,
                    ha='center', va='center',
                    fontsize=FS, bbox=_lbl(), zorder=3)

    # 正向箭头
    akw = dict(arrowstyle='->', lw=1.5, color='black', mutation_scale=16)
    for xf, xt in [(3.0, 4.0), (6.5, 7.5), (10.0, 11.0)]:
        ax.annotate('', xy=(xt, by + bh / 2), xytext=(xf, by + bh / 2),
                    arrowprops=akw)

    # 反馈虚线
    ax.annotate('', xy=(1.75, 2.15), xytext=(12.25, 2.15),
                arrowprops=dict(arrowstyle='->', lw=1.2, color='black',
                                mutation_scale=14, linestyle='dashed'))
    ax.text(7, 1.5, '反馈循环 (Feedback Loop)', ha='center', va='center',
            fontsize=FS, style='italic')

    fig.tight_layout()
    _save(fig, 'imoi-model.pdf')


# ============================================================
# 图 2.3  开放式创新模型
# ============================================================
def create_open_innovation_model():
    W = DISPLAY_W
    H = W * 0.78
    fig, ax = plt.subplots(figsize=(W, H))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # 企业边界虚线大框（加高，覆盖所有左右连接点 y=2.9~8.3）
    ax.add_patch(FancyBboxPatch((3.2, 2.2), 5.6, 6.8, boxstyle='round,pad=0.15',
                                facecolor='white', edgecolor='black',
                                linewidth=1.5, linestyle='--', zorder=0))
    ax.text(6, 8.65, '企业创新系统', ha='center', va='center',
            fontsize=FS, fontweight='bold', zorder=2)

    # 内部研发（网格），居中于大框内
    ax.add_patch(FancyBboxPatch((4.3, 4.0), 3.4, 2.4, boxstyle='round,pad=0.08',
                                facecolor='white', edgecolor='black',
                                linewidth=1.5, hatch='++', zorder=1))
    ax.text(6, 5.55, '内部研发', ha='center', va='center',
            fontsize=FS, fontweight='bold', bbox=_tbg(), zorder=2)
    ax.text(6, 4.8, 'Internal R&D', ha='center', va='center',
            fontsize=FS, fontfamily='Times New Roman', style='italic',
            bbox=_tbg(), zorder=2)

    # 左侧输入
    ax.text(1.3, 9.3, '外部知识输入', ha='center', va='center',
            fontsize=FS, fontweight='bold')

    in_data = [
        {'y': 8.3, 'text': '大学/研究机构', 'h': '//'},
        {'y': 6.5, 'text': '合作伙伴',     'h': '\\\\'},
        {'y': 4.7, 'text': '客户/用户',     'h': '..'},
        {'y': 2.9, 'text': '供应商',        'h': 'xx'},
    ]
    for d in in_data:
        ax.add_patch(FancyBboxPatch((0.1, d['y'] - 0.4), 2.4, 0.8,
                                    boxstyle='round,pad=0.05',
                                    facecolor='white', edgecolor='black',
                                    linewidth=1.2, hatch=d['h'], zorder=1))
        ax.text(1.3, d['y'], d['text'], ha='center', va='center',
                fontsize=FS, bbox=_tbg(), zorder=2)
        ax.annotate('', xy=(3.2, d['y']), xytext=(2.5, d['y']),
                    arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))

    # 右侧输出
    ax.text(10.7, 9.3, '创新成果输出', ha='center', va='center',
            fontsize=FS, fontweight='bold')

    out_data = [
        {'y': 8.3, 'text': '技术转让', 'h': '||'},
        {'y': 6.5, 'text': '开源项目', 'h': '--'},
        {'y': 4.7, 'text': '产品/服务', 'h': 'oo'},
        {'y': 2.9, 'text': '专利许可', 'h': '++'},
    ]
    for d in out_data:
        ax.add_patch(FancyBboxPatch((9.5, d['y'] - 0.4), 2.4, 0.8,
                                    boxstyle='round,pad=0.05',
                                    facecolor='white', edgecolor='black',
                                    linewidth=1.2, hatch=d['h'], zorder=1))
        ax.text(10.7, d['y'], d['text'], ha='center', va='center',
                fontsize=FS, bbox=_tbg(), zorder=2)
        ax.annotate('', xy=(9.5, d['y']), xytext=(8.8, d['y']),
                    arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))

    # 底部双向箭头
    ax.annotate('', xy=(2.5, 1.5), xytext=(9.5, 1.5),
                arrowprops=dict(arrowstyle='<->', lw=1.5, color='black'))
    ax.text(6, 1.0, '双向流动与协同创新', ha='center', va='center',
            fontsize=FS, fontweight='bold')

    fig.tight_layout()
    _save(fig, 'open-innovation-model.pdf')


def main():
    print("=" * 60)
    print("生成第二章图表（v5：字号+纹理+间距修正）")
    print("=" * 60)
    create_amo_framework()
    create_imoi_model()
    create_open_innovation_model()
    print("=" * 60)
    print("完成！")


if __name__ == '__main__':
    main()
