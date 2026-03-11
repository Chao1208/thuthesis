#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成波特五力模型图 - 用于第4.1.4节
针对百度公司的竞争环境分析
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.lines as mlines

# 设置中文字体和样式 - 增大字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'STHeiti']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.size'] = 12  # 增大基础字体

# 专业配色方案
COLORS = {
    'center': '#2E86AB',      # 中心 - 行业竞争
    'top': '#A23B72',         # 顶部 - 潜在进入者
    'bottom': '#F18F01',      # 底部 - 替代品
    'left': '#06A77D',        # 左侧 - 供应商
    'right': '#D2691E',       # 右侧 - 客户
    'arrow': '#666666',       # 箭头颜色
    'text': '#333333'         # 文字颜色
}

def create_porter_five_forces():
    """创建波特五力模型图"""
    
    fig, ax = plt.subplots(figsize=(16, 12))  # 增大画布
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # 定义各个力量的位置和大小
    # 中心：现有竞争者
    center_box = FancyBboxPatch(
        (3.5, 3.5), 3, 3,
        boxstyle="round,pad=0.1",
        edgecolor=COLORS['center'],
        facecolor=COLORS['center'],
        alpha=0.85,
        linewidth=3
    )
    ax.add_patch(center_box)
    
    # 顶部：潜在进入者威胁
    top_box = FancyBboxPatch(
        (3.5, 7.5), 3, 1.8,
        boxstyle="round,pad=0.08",
        edgecolor=COLORS['top'],
        facecolor=COLORS['top'],
        alpha=0.75,
        linewidth=2.5
    )
    ax.add_patch(top_box)
    
    # 底部：替代品威胁
    bottom_box = FancyBboxPatch(
        (3.5, 0.7), 3, 1.8,
        boxstyle="round,pad=0.08",
        edgecolor=COLORS['bottom'],
        facecolor=COLORS['bottom'],
        alpha=0.75,
        linewidth=2.5
    )
    ax.add_patch(bottom_box)
    
    # 左侧：供应商议价能力
    left_box = FancyBboxPatch(
        (0.5, 3.5), 2.2, 3,
        boxstyle="round,pad=0.08",
        edgecolor=COLORS['left'],
        facecolor=COLORS['left'],
        alpha=0.75,
        linewidth=2.5
    )
    ax.add_patch(left_box)
    
    # 右侧：客户议价能力
    right_box = FancyBboxPatch(
        (7.3, 3.5), 2.2, 3,
        boxstyle="round,pad=0.08",
        edgecolor=COLORS['right'],
        facecolor=COLORS['right'],
        alpha=0.75,
        linewidth=2.5
    )
    ax.add_patch(right_box)
    
    # 添加箭头（表示各力量对中心的影响）
    arrow_props = dict(
        arrowstyle='->',
        color=COLORS['arrow'],
        lw=2.5,
        alpha=0.7,
        mutation_scale=25
    )
    
    # 顶部箭头
    ax.annotate('', xy=(5, 6.5), xytext=(5, 7.5),
                arrowprops=arrow_props)
    
    # 底部箭头
    ax.annotate('', xy=(5, 3.5), xytext=(5, 2.5),
                arrowprops=arrow_props)
    
    # 左侧箭头
    ax.annotate('', xy=(3.5, 5), xytext=(2.7, 5),
                arrowprops=arrow_props)
    
    # 右侧箭头
    ax.annotate('', xy=(6.5, 5), xytext=(7.3, 5),
                arrowprops=arrow_props)
    
    # 添加文字标签
    # 中心
    ax.text(5, 5.6, '现有竞争者', 
            ha='center', va='center',
            fontsize=18, fontweight='bold', color='white')  # 增大
    ax.text(5, 5, '行业内竞争', 
            ha='center', va='center',
            fontsize=16, fontweight='bold', color='white')  # 增大
    
    # 添加中心详细内容
    center_details = [
        '• 字节跳动、阿里巴巴',
        '• 腾讯、华为（AI领域）',
        '• 特斯拉、小鹏（智能驾驶）',
        '• 竞争维度：技术、生态、人才'
    ]
    y_pos = 4.3
    for detail in center_details:
        ax.text(5, y_pos, detail,
                ha='center', va='center',
                fontsize=11, color='white')  # 增大到11
        y_pos -= 0.28
    
    # 顶部
    ax.text(5, 8.8, '潜在进入者威胁', 
            ha='center', va='center',
            fontsize=16, fontweight='bold', color='white')  # 增大
    ax.text(5, 8.3, '威胁程度：中低', 
            ha='center', va='center',
            fontsize=13, fontweight='bold', color='white',  # 增大
            style='italic')
    top_details = [
        '• 技术壁垒和资本壁垒较高',
        '• 专注型AI初创企业',
        '• OpenAI、Google等国际巨头'
    ]
    y_pos = 7.95
    for detail in top_details:
        ax.text(5, y_pos, detail,
                ha='center', va='center',
                fontsize=11, color='white')  # 增大到11
        y_pos -= 0.24
    
    # 底部
    ax.text(5, 2.2, '替代品威胁', 
            ha='center', va='center',
            fontsize=16, fontweight='bold', color='white')  # 增大
    ax.text(5, 1.8, '威胁程度：中', 
            ha='center', va='center',
            fontsize=13, fontweight='bold', color='white',  # 增大
            style='italic')
    bottom_details = [
        '• 对话式AI替代传统搜索',
        '• 短视频、直播分流广告',
        '• 技术范式转变风险'
    ]
    y_pos = 1.5
    for detail in bottom_details:
        ax.text(5, y_pos, detail,
                ha='center', va='center',
                fontsize=11, color='white')  # 增大到11
        y_pos -= 0.24
    
    # 左侧
    ax.text(1.6, 5.8, '供应商', 
            ha='center', va='center',
            fontsize=16, fontweight='bold', color='white')  # 增大
    ax.text(1.6, 5.4, '议价能力', 
            ha='center', va='center',
            fontsize=16, fontweight='bold', color='white')  # 增大
    ax.text(1.6, 4.9, '能力：中高', 
            ha='center', va='center',
            fontsize=13, fontweight='bold', color='white',  # 增大
            style='italic')
    left_details = [
        '芯片供应商',
        '云计算资源',
        'AI人才市场',
        '断供风险',
        '人力成本上升'
    ]
    y_pos = 4.5
    for detail in left_details:
        ax.text(1.6, y_pos, f'• {detail}',
                ha='center', va='center',
                fontsize=10, color='white')  # 增大到10
        y_pos -= 0.32
    
    # 右侧
    ax.text(8.4, 5.8, '客户', 
            ha='center', va='center',
            fontsize=16, fontweight='bold', color='white')  # 增大
    ax.text(8.4, 5.4, '议价能力', 
            ha='center', va='center',
            fontsize=16, fontweight='bold', color='white')  # 增大
    ax.text(8.4, 4.9, '能力：差异化', 
            ha='center', va='center',
            fontsize=13, fontweight='bold', color='white',  # 增大
            style='italic')
    right_details = [
        'To C：转换成本低',
        'To B：大客户议价强',
        'To G：决策复杂',
        '定制化需求',
        '技术成熟度要求高'
    ]
    y_pos = 4.5
    for detail in right_details:
        ax.text(8.4, y_pos, f'• {detail}',
                ha='center', va='center',
                fontsize=10, color='white')  # 增大到10
        y_pos -= 0.32
    
    # 添加标题
    plt.title('百度公司竞争环境分析——波特五力模型', 
             fontsize=22, fontweight='bold', pad=20,  # 增大标题
             color=COLORS['text'])
    
    # 添加图例说明
    legend_elements = [
        mlines.Line2D([0], [0], color=COLORS['center'], lw=8, 
                     label='行业内竞争（核心）'),
        mlines.Line2D([0], [0], color=COLORS['top'], lw=8, 
                     label='潜在进入者威胁'),
        mlines.Line2D([0], [0], color=COLORS['bottom'], lw=8, 
                     label='替代品威胁'),
        mlines.Line2D([0], [0], color=COLORS['left'], lw=8, 
                     label='供应商议价能力'),
        mlines.Line2D([0], [0], color=COLORS['right'], lw=8, 
                     label='客户议价能力')
    ]
    ax.legend(handles=legend_elements, loc='upper left', 
             fontsize=12, framealpha=0.95,  # 增大图例字体
             bbox_to_anchor=(-0.02, 1.05))
    
    # 移除数据来源说明（按用户要求删除）
    
    plt.tight_layout()
    plt.savefig('porter-five-forces-baidu.pdf', 
                bbox_inches='tight', dpi=300, 
                facecolor='white', edgecolor='none')
    print("✓ 已生成波特五力模型图: porter-five-forces-baidu.pdf")
    plt.close()


def main():
    """主函数"""
    print("="*60)
    print("开始生成波特五力模型图...")
    print("="*60)
    
    try:
        create_porter_five_forces()
        
        print("="*60)
        print("图表生成完成！")
        print("生成的文件：porter-five-forces-baidu.pdf")
        print("="*60)
        print("请将此PDF文件保存在 myfigure/ 文件夹")
        print("然后在 chap04.tex 的第4.1.4节后添加图表引用")
        print("="*60)
        
    except Exception as e:
        print(f"生成图表时出错: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()


