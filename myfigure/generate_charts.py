#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成第三章所需的图表
用于论文《新环境下互联网公司研发团队管理的现状与困境》
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# 设置中文字体和样式
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'STHeiti']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300

# 设置专业的配色方案
COLORS = {
    'primary': '#2E86AB',
    'secondary': '#A23B72',
    'tertiary': '#F18F01',
    'success': '#06A77D',
    'warning': '#D2691E',
    'info': '#4682B4'
}

def generate_fig_1():
    """
    图3.1 中国互联网网民规模与互联网企业数量增长趋势（2000-2010）
    双Y轴折线图
    """
    years = np.array([2000, 2002, 2004, 2006, 2008, 2010])
    netizens = np.array([0.23, 0.59, 0.94, 1.37, 2.98, 4.57])  # 亿人
    companies = np.array([0.1, 0.18, 0.35, 0.62, 1.2, 2.0])  # 万家
    
    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax2 = ax1.twinx()
    
    # 绘制网民规模曲线
    line1 = ax1.plot(years, netizens, 'o-', color=COLORS['primary'], 
                     linewidth=2.5, markersize=9, label='网民规模',
                     markerfacecolor=COLORS['primary'], markeredgecolor='white', 
                     markeredgewidth=1.5)
    
    # 绘制企业数量曲线
    line2 = ax2.plot(years, companies, 's-', color=COLORS['secondary'], 
                     linewidth=2.5, markersize=9, label='企业数量',
                     markerfacecolor=COLORS['secondary'], markeredgecolor='white',
                     markeredgewidth=1.5)
    
    # 设置标签
    ax1.set_xlabel('年份', fontsize=13, fontweight='bold')
    ax1.set_ylabel('网民规模（亿人）', fontsize=13, fontweight='bold', 
                   color=COLORS['primary'])
    ax2.set_ylabel('互联网企业数量（万家）', fontsize=13, fontweight='bold', 
                   color=COLORS['secondary'])
    
    # 设置刻度颜色
    ax1.tick_params(axis='y', labelcolor=COLORS['primary'], labelsize=11)
    ax2.tick_params(axis='y', labelcolor=COLORS['secondary'], labelsize=11)
    ax1.tick_params(axis='x', labelsize=11)
    
    # 添加网格
    ax1.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
    
    # 添加数据标签
    for x, y in zip(years, netizens):
        ax1.text(x, y + 0.15, f'{y:.2f}', ha='center', va='bottom', 
                fontsize=9, color=COLORS['primary'])
    
    for x, y in zip(years, companies):
        ax2.text(x, y + 0.08, f'{y:.2f}', ha='center', va='bottom', 
                fontsize=9, color=COLORS['secondary'])
    
    # 设置标题
    plt.title('中国互联网网民规模与企业数量增长趋势（2000-2010）', 
             fontsize=14, fontweight='bold', pad=15)
    
    # 合并图例
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper left', fontsize=11, framealpha=0.9)
    
    # 设置坐标轴范围
    ax1.set_ylim(0, 5.5)
    ax2.set_ylim(0, 2.5)
    
    plt.tight_layout()
    plt.savefig('internet-development-2000-2010.pdf', bbox_inches='tight', dpi=300)
    print("✓ 已生成图3.1: internet-development-2000-2010.pdf")
    plt.close()


def generate_fig_2():
    """
    图3.2 中国互联网百强企业研发投入增长趋势（2010-2020）
    柱状图+折线图组合
    """
    years = np.array([2010, 2012, 2014, 2016, 2018, 2020])
    investment = np.array([200, 320, 480, 720, 1200, 1898])  # 亿元
    ratio_low = np.array([10, 10.5, 11, 12, 13.5, 15])  # 研发投入占比下限
    ratio_high = np.array([12, 13, 14, 15, 17, 20])  # 研发投入占比上限
    ratio_avg = (ratio_low + ratio_high) / 2
    
    fig, ax1 = plt.subplots(figsize=(11, 6))
    ax2 = ax1.twinx()
    
    # 绘制柱状图
    bars = ax1.bar(years, investment, width=1.2, color=COLORS['primary'], 
                   alpha=0.7, edgecolor='white', linewidth=1.5,
                   label='研发投入总额')
    
    # 绘制折线图（使用范围带）
    line = ax2.plot(years, ratio_avg, 'o-', color=COLORS['secondary'], 
                    linewidth=2.5, markersize=9, label='研发投入占比',
                    markerfacecolor=COLORS['secondary'], markeredgecolor='white',
                    markeredgewidth=1.5)
    ax2.fill_between(years, ratio_low, ratio_high, color=COLORS['secondary'], 
                     alpha=0.2)
    
    # 设置标签
    ax1.set_xlabel('年份', fontsize=13, fontweight='bold')
    ax1.set_ylabel('研发投入总额（亿元）', fontsize=13, fontweight='bold', 
                   color=COLORS['primary'])
    ax2.set_ylabel('研发投入占营收比（%）', fontsize=13, fontweight='bold', 
                   color=COLORS['secondary'])
    
    # 设置刻度颜色
    ax1.tick_params(axis='y', labelcolor=COLORS['primary'], labelsize=11)
    ax2.tick_params(axis='y', labelcolor=COLORS['secondary'], labelsize=11)
    ax1.tick_params(axis='x', labelsize=11)
    
    # 添加网格
    ax1.grid(True, alpha=0.3, linestyle='--', linewidth=0.5, axis='y')
    
    # 添加数据标签
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 50,
                f'{int(height)}', ha='center', va='bottom', 
                fontsize=9, color=COLORS['primary'], fontweight='bold')
    
    for x, y in zip(years, ratio_avg):
        ax2.text(x, y + 0.5, f'{y:.1f}%', ha='center', va='bottom', 
                fontsize=9, color=COLORS['secondary'])
    
    # 设置标题
    plt.title('中国互联网百强企业研发投入增长趋势（2010-2020）', 
             fontsize=14, fontweight='bold', pad=15)
    
    # 合并图例
    ax1.legend(loc='upper left', fontsize=11, framealpha=0.9)
    ax2.legend(loc='upper center', fontsize=11, framealpha=0.9)
    
    # 设置坐标轴范围
    ax1.set_ylim(0, 2200)
    ax2.set_ylim(0, 25)
    
    plt.tight_layout()
    plt.savefig('rnd-investment-growth.pdf', bbox_inches='tight', dpi=300)
    print("✓ 已生成图3.2: rnd-investment-growth.pdf")
    plt.close()


def generate_fig_3():
    """
    图3.3 中国互联网企业敏捷开发方法应用情况（2023）
    水平条形图
    """
    methods = ['Scrum', '看板\n(Kanban)', 'SAFe\n(规模化敏捷)', 'XP\n(极限编程)', '其他敏捷\n方法']
    percentages = [68, 35, 28, 18, 12]
    
    # 颜色渐变
    colors = [COLORS['primary'], COLORS['info'], COLORS['success'], 
              COLORS['warning'], COLORS['secondary']]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 绘制水平条形图
    y_pos = np.arange(len(methods))
    bars = ax.barh(y_pos, percentages, color=colors, alpha=0.8, 
                   edgecolor='white', linewidth=2)
    
    # 添加基准线（50%）
    ax.axvline(x=50, color='red', linestyle='--', linewidth=2, 
               alpha=0.6, label='50%基准线')
    
    # 设置标签
    ax.set_yticks(y_pos)
    ax.set_yticklabels(methods, fontsize=12)
    ax.set_xlabel('应用率（%）', fontsize=13, fontweight='bold')
    ax.set_ylabel('敏捷方法类型', fontsize=13, fontweight='bold')
    
    # 添加数据标签
    for i, (bar, pct) in enumerate(zip(bars, percentages)):
        width = bar.get_width()
        ax.text(width + 2, bar.get_y() + bar.get_height()/2, 
                f'{pct}%', ha='left', va='center', 
                fontsize=11, fontweight='bold', color=colors[i])
    
    # 设置标题
    plt.title('中国互联网企业敏捷开发方法应用情况（2023）', 
             fontsize=14, fontweight='bold', pad=15)
    
    # 添加网格
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5, axis='x')
    ax.set_axisbelow(True)
    
    # 设置坐标轴范围
    ax.set_xlim(0, 80)
    
    # 添加图例
    ax.legend(loc='lower right', fontsize=10, framealpha=0.9)
    
    plt.tight_layout()
    plt.savefig('agile-adoption-rate.pdf', bbox_inches='tight', dpi=300)
    print("✓ 已生成图3.3: agile-adoption-rate.pdf")
    plt.close()


def generate_fig_4():
    """
    图3.4 互联网企业创新激励机制构成（2023）
    饼图
    """
    labels = ['薪酬福利', '股权激励', '项目奖金', '晋升通道', '创新时间/基金']
    sizes = [35, 25, 18, 12, 10]
    colors = [COLORS['primary'], COLORS['secondary'], COLORS['tertiary'], 
              COLORS['success'], COLORS['warning']]
    explode = (0.05, 0.02, 0, 0, 0)  # 突出显示最大的扇区
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # 绘制饼图
    wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, 
                                       colors=colors, autopct='%1.1f%%',
                                       startangle=90, 
                                       textprops={'fontsize': 12, 'fontweight': 'bold'},
                                       wedgeprops={'edgecolor': 'white', 'linewidth': 2})
    
    # 设置百分比文字样式
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(11)
        autotext.set_fontweight('bold')
    
    # 设置标签文字样式
    for text in texts:
        text.set_fontsize(12)
        text.set_fontweight('bold')
    
    # 设置标题
    plt.title('互联网企业创新激励机制构成（2023）', 
             fontsize=14, fontweight='bold', pad=20)
    
    # 添加说明
    plt.text(0, -1.4, '数据来源：麦肯锡公司《中国科技人才市场趋势报告》（2023）', 
            ha='center', fontsize=9, style='italic', color='gray')
    
    plt.tight_layout()
    plt.savefig('innovation-incentive-system.pdf', bbox_inches='tight', dpi=300)
    print("✓ 已生成图3.4: innovation-incentive-system.pdf")
    plt.close()


def main():
    """主函数：生成所有图表"""
    print("="*60)
    print("开始生成第三章图表...")
    print("="*60)
    
    try:
        generate_fig_1()
        generate_fig_2()
        generate_fig_3()
        generate_fig_4()
        
        print("="*60)
        print("所有图表生成完成！")
        print("生成的文件：")
        print("  1. internet-development-2000-2010.pdf")
        print("  2. rnd-investment-growth.pdf")
        print("  3. agile-adoption-rate.pdf")
        print("  4. innovation-incentive-system.pdf")
        print("="*60)
        print("请将这些PDF文件复制到 myfigure/ 文件夹")
        print("然后在 chap03.tex 中取消注释 \\includegraphics 命令")
        print("="*60)
        
    except Exception as e:
        print(f"生成图表时出错: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()


