#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成第二章理论综述的图表
包括：AMO框架、IMOI模型、开放式创新模型
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import matplotlib.lines as mlines
import numpy as np

# 设置中文字体和样式
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'STHeiti']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300

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


def create_amo_framework():
    """创建AMO框架图"""
    fig, ax = plt.subplots(figsize=(12, 8))
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
           fontsize=18, fontweight='bold', color='white')
    
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
           fontsize=16, fontweight='bold', color='white')
    ax.text(2.5, 7.2, 'Ability', 
           ha='center', va='center',
           fontsize=12, color='white', style='italic')
    
    # Motivation - 动机
    motivation_circle = Circle((7.5, 7.5), 1, 
                              facecolor=COLORS['tertiary'], 
                              edgecolor='white',
                              linewidth=2.5,
                              alpha=0.85)
    ax.add_patch(motivation_circle)
    ax.text(7.5, 7.8, '动机', 
           ha='center', va='center',
           fontsize=16, fontweight='bold', color='white')
    ax.text(7.5, 7.2, 'Motivation', 
           ha='center', va='center',
           fontsize=12, color='white', style='italic')
    
    # Opportunity - 机会
    opportunity_circle = Circle((5, 2.5), 1, 
                               facecolor=COLORS['success'], 
                               edgecolor='white',
                               linewidth=2.5,
                               alpha=0.85)
    ax.add_patch(opportunity_circle)
    ax.text(5, 2.8, '机会', 
           ha='center', va='center',
           fontsize=16, fontweight='bold', color='white')
    ax.text(5, 2.2, 'Opportunity', 
           ha='center', va='center',
           fontsize=12, color='white', style='italic')
    
    # 添加箭头连接
    arrow_props = dict(
        arrowstyle='->',
        lw=2.5,
        alpha=0.7,
        mutation_scale=20
    )
    
    # 从能力到绩效
    ax.annotate('', xy=(4.2, 5.8), xytext=(3.2, 6.8),
                arrowprops={**arrow_props, 'color': COLORS['secondary']})
    
    # 从动机到绩效
    ax.annotate('', xy=(5.8, 5.8), xytext=(6.8, 6.8),
                arrowprops={**arrow_props, 'color': COLORS['tertiary']})
    
    # 从机会到绩效
    ax.annotate('', xy=(5, 3.7), xytext=(5, 3.5),
                arrowprops={**arrow_props, 'color': COLORS['success']})
    
    # 添加详细说明
    # 能力说明
    ability_text = [
        '• 知识水平',
        '• 技能熟练度',
        '• 专业能力',
        '• 学习能力'
    ]
    y_pos = 9.3
    for text in ability_text:
        ax.text(2.5, y_pos, text,
               ha='center', va='center',
               fontsize=9, color=COLORS['secondary'],
               bbox=dict(boxstyle='round,pad=0.3', 
                        facecolor='white', 
                        edgecolor=COLORS['secondary'],
                        alpha=0.8))
        y_pos -= 0.35
    
    # 动机说明
    motivation_text = [
        '• 内在动机',
        '• 外在激励',
        '• 工作热情',
        '• 目标导向'
    ]
    y_pos = 9.3
    for text in motivation_text:
        ax.text(7.5, y_pos, text,
               ha='center', va='center',
               fontsize=9, color=COLORS['tertiary'],
               bbox=dict(boxstyle='round,pad=0.3', 
                        facecolor='white', 
                        edgecolor=COLORS['tertiary'],
                        alpha=0.8))
        y_pos -= 0.35
    
    # 机会说明
    opportunity_text = [
        '• 参与决策',
        '• 资源支持',
        '• 成长机会',
        '• 工作自主性'
    ]
    x_pos = 2.8
    for text in opportunity_text:
        ax.text(x_pos, 1.2, text,
               ha='center', va='center',
               fontsize=9, color=COLORS['success'],
               bbox=dict(boxstyle='round,pad=0.3', 
                        facecolor='white', 
                        edgecolor=COLORS['success'],
                        alpha=0.8))
        x_pos += 1.5
    
    # 添加标题
    plt.title('AMO框架：员工绩效的三要素模型', 
             fontsize=18, fontweight='bold', pad=15)
    
    # 添加说明文字
    ax.text(5, 0.3, '数据来源：Bos-Nehles et al. (2023), 汤超颖等(2022)', 
           ha='center', va='center',
           fontsize=9, style='italic', color='gray')
    
    plt.tight_layout()
    plt.savefig('amo-framework.pdf', 
               bbox_inches='tight', dpi=300,
               facecolor='white', edgecolor='none')
    print("✓ 已生成图2.1: amo-framework.pdf")
    plt.close()


def create_imoi_model():
    """创建I-M-O-I团队效能模型图"""
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    # 定义四个阶段的框
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
               fontsize=14, fontweight='bold', color='white')
    
    # 添加箭头
    arrow_props = dict(
        arrowstyle='->',
        lw=3,
        alpha=0.8,
        mutation_scale=25
    )
    
    # Input -> Mediator
    ax.annotate('', xy=(4, 3), xytext=(3, 3),
               arrowprops={**arrow_props, 'color': '#666666'})
    
    # Mediator -> Output
    ax.annotate('', xy=(7.5, 3), xytext=(6.5, 3),
               arrowprops={**arrow_props, 'color': '#666666'})
    
    # Output -> Input (反馈环)
    ax.annotate('', xy=(11, 3), xytext=(10, 3),
               arrowprops={**arrow_props, 'color': '#666666'})
    
    # 反馈箭头（从右侧回到左侧）
    ax.annotate('', xy=(1.75, 1.8), xytext=(12.25, 1.8),
               arrowprops={**arrow_props, 'color': COLORS['warning'],
                          'linestyle': 'dashed', 'lw': 2.5})
    ax.text(7, 1.3, '反馈循环', 
           ha='center', va='center',
           fontsize=11, color=COLORS['warning'],
           fontweight='bold', style='italic')
    
    # 添加详细内容
    input_items = [
        '组织情境', '团队特征', '个体特征'
    ]
    y_pos = 4.5
    for item in input_items:
        ax.text(1.75, y_pos, f'• {item}',
               ha='center', va='center',
               fontsize=9, color='white')
        y_pos += 0.3
    
    mediator_items = [
        '团队过程', '涌现状态', '协作机制'
    ]
    y_pos = 4.5
    for item in mediator_items:
        ax.text(5.25, y_pos, f'• {item}',
               ha='center', va='center',
               fontsize=9, color='white')
        y_pos += 0.3
    
    output_items = [
        '团队绩效', '成员满意度', '创新产出'
    ]
    y_pos = 4.5
    for item in output_items:
        ax.text(8.75, y_pos, f'• {item}',
               ha='center', va='center',
               fontsize=9, color='white')
        y_pos += 0.3
    
    # 添加标题
    plt.title('I-M-O-I团队效能循环模型', 
             fontsize=18, fontweight='bold', pad=15)
    
    # 添加说明文字
    ax.text(7, 0.3, '数据来源：Mathieu et al. (2008)', 
           ha='center', va='center',
           fontsize=9, style='italic', color='gray')
    
    plt.tight_layout()
    plt.savefig('imoi-model.pdf', 
               bbox_inches='tight', dpi=300,
               facecolor='white', edgecolor='none')
    print("✓ 已生成图2.2: imoi-model.pdf")
    plt.close()


def create_open_innovation_model():
    """创建开放式创新模型图"""
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # 中央企业框
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
           fontsize=16, fontweight='bold', 
           color=COLORS['primary'])
    
    # 内部研发
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
           fontsize=14, fontweight='bold', color='white')
    ax.text(6, 4.6, 'Internal R&D', 
           ha='center', va='center',
           fontsize=11, color='white', style='italic')
    
    # 外部输入源（左侧）
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
               fontsize=11, fontweight='bold', color='white')
        
        # 箭头指向企业
        ax.annotate('', xy=(3, inp['y']), xytext=(2.3, inp['y']),
                   arrowprops=dict(arrowstyle='->', lw=2, 
                                  color=inp['color'], alpha=0.7))
    
    # 外部输出（右侧）
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
               fontsize=11, fontweight='bold', color='white')
        
        # 箭头从企业指出
        ax.annotate('', xy=(9.7, out['y']), xytext=(9, out['y']),
                   arrowprops=dict(arrowstyle='->', lw=2, 
                                  color=out['color'], alpha=0.7))
    
    # 添加标签
    ax.text(1.3, 9.5, '外部知识输入', 
           ha='center', va='center',
           fontsize=13, fontweight='bold', 
           color=COLORS['success'])
    
    ax.text(10.7, 9.5, '创新成果输出', 
           ha='center', va='center',
           fontsize=13, fontweight='bold', 
           color=COLORS['tertiary'])
    
    # 双向箭头表示互动
    ax.text(6, 1.5, '↔', 
           ha='center', va='center',
           fontsize=30, color=COLORS['primary'])
    ax.text(6, 0.9, '双向流动与协同创新', 
           ha='center', va='center',
           fontsize=12, fontweight='bold', 
           color=COLORS['primary'])
    
    # 添加标题
    plt.title('开放式创新模型（Chesbrough）', 
             fontsize=18, fontweight='bold', pad=15)
    
    # 添加说明文字
    ax.text(6, 0.2, '数据来源：Chesbrough (2003), 高良谋和马文甲(2014), 张震宇和陈劲(2008)', 
           ha='center', va='center',
           fontsize=8, style='italic', color='gray')
    
    plt.tight_layout()
    plt.savefig('open-innovation-model.pdf', 
               bbox_inches='tight', dpi=300,
               facecolor='white', edgecolor='none')
    print("✓ 已生成图2.3: open-innovation-model.pdf")
    plt.close()


def main():
    """主函数"""
    print("="*60)
    print("开始生成第二章理论综述图表...")
    print("="*60)
    
    try:
        create_amo_framework()
        create_imoi_model()
        create_open_innovation_model()
        
        print("="*60)
        print("所有图表生成完成！")
        print("生成的文件：")
        print("  1. amo-framework.pdf - AMO框架图")
        print("  2. imoi-model.pdf - IMOI团队效能模型")
        print("  3. open-innovation-model.pdf - 开放式创新模型")
        print("="*60)
        print("请将这些PDF文件保存在 myfigure/ 文件夹")
        print("然后在 chap02.tex 中添加图表引用")
        print("="*60)
        
    except Exception as e:
        print(f"生成图表时出错: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()


