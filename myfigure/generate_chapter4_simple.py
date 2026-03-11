#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成第四章图表（简化版本）
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, FancyArrowPatch
import numpy as np

# 字体设置（优先使用系统中文字体）
plt.rcParams['font.sans-serif'] = ['SimHei', 'STHeiti', 'PingFang SC', 'Microsoft YaHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 11

def create_org_evolution():
    """百度组织架构演变图"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))
    
    # 左图: 烟囱式架构
    ax1 = axes[0]
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title('（a）调整前：烟囱式架构', fontsize=14, fontweight='bold', pad=20)
    
    # 绘制烟囱式部门
    departments = ['语音', '图像', '文本', '知识图谱', 'NLP', '推荐', '广告', '搜索']
    colors = plt.cm.Set3(np.linspace(0, 1, len(departments)))
    
    for i, (dept, color) in enumerate(zip(departments, colors)):
        x = 1 + (i % 4) * 2
        y = 7 - (i // 4) * 3
        rect = FancyBboxPatch((x-0.7, y-0.8), 1.4, 1.6,
                             boxstyle="round,pad=0.1", 
                             facecolor=color, edgecolor='#333333', linewidth=1.5)
        ax1.add_patch(rect)
        ax1.text(x, y, dept, ha='center', va='center', fontsize=9, fontweight='bold')
    
    # 添加问题标注
    ax1.text(5, 9, '沟通壁垒\n部门墙', ha='center', fontsize=10, color='red',
            fontweight='bold', bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
    
    # 右图: BMU/AMU架构
    ax2 = axes[1]
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title('（b）调整后：BMU/AMU双BU架构', fontsize=14, fontweight='bold', pad=20)
    
    # BMU
    bmu = FancyBboxPatch((1, 5.5), 3.5, 3, boxstyle="round,pad=0.15",
                         facecolor='#3498db', edgecolor='#2c3e50', linewidth=2)
    ax2.add_patch(bmu)
    ax2.text(2.75, 7.2, 'BMU\n基础模型与理解', ha='center', va='center', 
             fontsize=10, fontweight='bold', color='white')
    
    # AMU
    amu = FancyBboxPatch((5.5, 5.5), 3.5, 3, boxstyle="round,pad=0.15",
                         facecolor='#e74c3c', edgecolor='#2c3e50', linewidth=2)
    ax2.add_patch(amu)
    ax2.text(7.25, 7.2, 'AMU\n应用与多模态', ha='center', va='center', 
             fontsize=10, fontweight='bold', color='white')
    
    # Platform layer
    platform = FancyBboxPatch((2.5, 3), 5, 1.5, boxstyle="round,pad=0.1",
                              facecolor='#2ecc71', edgecolor='#27ae60', linewidth=2)
    ax2.add_patch(platform)
    ax2.text(5, 3.75, '共性平台层：飞桨 | 百度大脑 | AI中台', 
             ha='center', va='center', fontsize=9, fontweight='bold', color='white')
    
    # Business scenarios
    scenarios = ['搜索', '智能云', 'Apollo', '智能设备']
    for i, scenario in enumerate(scenarios):
        x = 1.5 + i * 2
        rect = FancyBboxPatch((x-0.7, 0.8), 1.4, 1.2, boxstyle="round,pad=0.08",
                              facecolor='#f39c12', edgecolor='#d68910', linewidth=1.5)
        ax2.add_patch(rect)
        ax2.text(x, 1.4, scenario, ha='center', va='center', fontsize=9, fontweight='bold')
    
    # Add flow arrows
    ax2.annotate('', xy=(5, 5.5), xytext=(5, 4.5),
                arrowprops=dict(arrowstyle='<->', color='#34495e', lw=2))
    
    # Collaboration label
    ax2.text(5, 9, '统一规划\n协同高效', ha='center', fontsize=10, 
             color='green', fontweight='bold',
             bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    
    plt.tight_layout()
    plt.savefig('baidu-org-evolution.pdf', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: baidu-org-evolution.pdf")


def create_swot_radar():
    """SWOT雷达图"""
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))
    
    categories = ['SO\n优势-机会', 'WO\n劣势-机会', 'WT\n劣势-威胁', 'ST\n优势-威胁']
    N = len(categories)
    
    # Data
    baidu_scores = [4.15, 3.85, 2.10, 2.40]
    industry_avg = [3.50, 3.20, 2.80, 2.60]
    benchmark = [4.30, 3.60, 2.40, 2.80]
    
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]
    
    baidu_scores += baidu_scores[:1]
    industry_avg += industry_avg[:1]
    benchmark += benchmark[:1]
    
    ax.plot(angles, baidu_scores, 'o-', linewidth=2.5, label='百度', color='#e74c3c')
    ax.fill(angles, baidu_scores, alpha=0.25, color='#e74c3c')
    
    ax.plot(angles, industry_avg, 's--', linewidth=2, label='行业平均', color='#95a5a6')
    ax.fill(angles, industry_avg, alpha=0.15, color='#95a5a6')
    
    ax.plot(angles, benchmark, '^:', linewidth=2, label='标杆企业', color='#3498db')
    ax.fill(angles, benchmark, alpha=0.15, color='#3498db')
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=10)
    ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    
    ax.set_title('百度研发管理SWOT战略四象限分析', fontsize=14, fontweight='bold', pad=20)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.savefig('swot-radar-baidu.pdf', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: swot-radar-baidu.pdf")


def create_amo_comparison():
    """AMO对比热力图"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    companies = ['百度', '阿里巴巴', '腾讯', '字节跳动', '行业平均']
    dimensions = ['能力(A)', '动机(M)', '机会(O)']
    
    data = np.array([
        [3.8, 3.2, 3.5],
        [4.0, 3.8, 3.8],
        [3.9, 3.6, 3.7],
        [4.2, 4.0, 4.1],
        [3.5, 3.4, 3.5],
    ])
    
    im = ax.imshow(data.T, cmap='RdYlGn', aspect='auto', vmin=2.5, vmax=4.5)
    
    ax.set_xticks(np.arange(len(companies)))
    ax.set_yticks(np.arange(len(dimensions)))
    ax.set_xticklabels(companies, fontsize=10)
    ax.set_yticklabels(dimensions, fontsize=10)
    
    for i in range(len(companies)):
        for j in range(len(dimensions)):
            text = ax.text(i, j, f'{data[i, j]:.1f}',
                          ha="center", va="center", color="black", fontweight='bold', fontsize=11)
    
    ax.set_title('AMO三维度：百度与行业对比', fontsize=14, fontweight='bold')
    
    cbar = plt.colorbar(im, ax=ax, shrink=0.8)
    cbar.set_label('得分（1-5分）', fontsize=10)
    
    plt.tight_layout()
    plt.savefig('amo-comparison.pdf', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: amo-comparison.pdf")


def create_dual_channel():
    """双通道职业发展"""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    ax.text(5, 9.5, '百度研发人员双通道职业发展体系', fontsize=15, 
            ha='center', fontweight='bold')
    
    # 管理通道
    mgmt_levels = [
        ('首席技术官(CTO)', 8.5, '#2c3e50'),
        ('副总裁(VP)', 7.2, '#34495e'),
        ('高级总监', 5.9, '#5d6d7e'),
        ('总监', 4.6, '#85929e'),
        ('高级经理', 3.3, '#aeb6bf'),
        ('经理', 2.0, '#d5d8dc'),
    ]
    
    for label, y, color in mgmt_levels:
        rect = FancyBboxPatch((1, y-0.4), 3, 0.8, boxstyle="round,pad=0.08",
                              facecolor=color, edgecolor='black', linewidth=1.5)
        ax.add_patch(rect)
        ax.text(2.5, y, label, ha='center', va='center', fontsize=9, 
                color='white' if y > 5 else 'black', fontweight='bold')
    
    # 技术通道
    tech_levels = [
        ('杰出科学家(Fellow)', 8.5, '#8e44ad'),
        ('资深科学家', 7.2, '#9b59b6'),
        ('高级科学家', 5.9, '#af7ac5'),
        ('科学家', 4.6, '#c39bd3'),
        ('资深工程师', 3.3, '#d7bde2'),
        ('高级工程师', 2.0, '#ebdef0'),
    ]
    
    for label, y, color in tech_levels:
        rect = FancyBboxPatch((6, y-0.4), 3, 0.8, boxstyle="round,pad=0.08",
                              facecolor=color, edgecolor='black', linewidth=1.5)
        ax.add_patch(rect)
        ax.text(7.5, y, label, ha='center', va='center', fontsize=9, 
                color='white' if y > 5 else 'black', fontweight='bold')
    
    ax.text(2.5, 1.0, '管理通道', ha='center', fontsize=12, fontweight='bold', color='#2c3e50')
    ax.text(7.5, 1.0, '技术通道', ha='center', fontsize=12, fontweight='bold', color='#8e44ad')
    
    # 双向流动
    for y in [2.0, 3.3, 4.6]:
        ax.annotate('', xy=(5.9, y), xytext=(4.1, y),
                   arrowprops=dict(arrowstyle='<->', color='#e67e22', lw=2))
    
    ax.text(5, 1.6, '双向流动通道', ha='center', fontsize=10, color='#e67e22', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('dual-career-channel.pdf', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: dual-career-channel.pdf")


def create_rd_dashboard():
    """研发效能仪表盘"""
    fig = plt.figure(figsize=(15, 10))
    fig.suptitle('百度研发效能综合仪表盘', fontsize=16, fontweight='bold')
    
    # 创建子图布局 (2,3)网格
    gs = fig.add_gridspec(2, 3, hspace=0.3, wspace=0.3)
    
    # 1. 交付效率 (左上)
    ax1 = fig.add_subplot(gs[0, 0])
    metrics = ['需求周期', '迭代完成率', '发布频率', '代码提交']
    current = [8.5, 88, 2.1, 1250]
    target = [10, 90, 2.5, 1500]
    x = np.arange(len(metrics))
    width = 0.35
    ax1.bar(x - width/2, current, width, label='当前', color='#3498db')
    ax1.bar(x + width/2, target, width, label='目标', color='#e74c3c', alpha=0.6)
    ax1.set_title('交付效率指标')
    ax1.set_xticks(x)
    ax1.set_xticklabels(metrics, rotation=15, ha='right', fontsize=9)
    ax1.legend(fontsize=8)
    
    # 2. 质量指标 (中上)
    ax2 = fig.add_subplot(gs[0, 1])
    quality_metrics = ['线上故障', '评审通过率', '测试覆盖率', 'TD密度']
    values = [12, 94, 78, 0.35]
    colors = ['#e74c3c' if v > 10 else '#2ecc71' if v > 90 else '#f39c12' for v in values]
    ax2.bar(quality_metrics, values, color=colors)
    ax2.set_title('质量指标')
    ax2.set_xticks(range(len(quality_metrics)))
    ax2.set_xticklabels(quality_metrics, rotation=15, ha='right', fontsize=9)
    
    # 3. 资源分配饼图 (右上)
    ax3 = fig.add_subplot(gs[0, 2])
    labels = ['新功能', 'TD偿还', '技术预研', '运营支持']
    sizes = [55, 20, 15, 10]
    colors_pie = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']
    ax3.pie(sizes, labels=labels, colors=colors_pie, autopct='%1.0f%%', startangle=90)
    ax3.set_title('研发资源分配')
    
    # 4. 趋势图 (左下)
    ax4 = fig.add_subplot(gs[1, 0])
    months = ['1月', '2月', '3月', '4月', '5月', '6月']
    efficiency = [2.4, 2.5, 2.6, 2.5, 2.7, 2.65]
    quality_trend = [3.2, 3.3, 3.1, 3.4, 3.5, 3.45]
    ax4.plot(months, efficiency, 'o-', label='交付效率指数', linewidth=2, color='#3498db')
    ax4.plot(months, quality_trend, 's-', label='质量指数', linewidth=2, color='#2ecc71')
    ax4.set_title('近6个月趋势')
    ax4.legend(fontsize=8)
    ax4.grid(True, alpha=0.3)
    
    # 5. 团队对比热力图 (中下+右下)
    ax5 = fig.add_subplot(gs[1, 1:])
    teams = ['搜索团队', '推荐团队', '云团队', 'Apollo', '大模型']
    indicators = ['交付效率', '代码质量', '创新产出', '协作效率', 'TD控制']
    heatmap_data = np.array([
        [4.2, 4.0, 3.5, 3.8, 3.2],
        [3.8, 3.5, 4.0, 3.5, 3.0],
        [3.5, 4.2, 3.8, 3.2, 4.0],
        [3.2, 3.8, 4.5, 3.0, 3.5],
        [4.0, 3.5, 4.8, 3.8, 2.8],
    ])
    im = ax5.imshow(heatmap_data, cmap='RdYlGn', aspect='auto', vmin=2, vmax=5)
    ax5.set_xticks(np.arange(len(indicators)))
    ax5.set_yticks(np.arange(len(teams)))
    ax5.set_xticklabels(indicators, fontsize=9)
    ax5.set_yticklabels(teams, fontsize=9)
    for i in range(len(teams)):
        for j in range(len(indicators)):
            ax5.text(j, i, f'{heatmap_data[i, j]:.1f}', ha="center", va="center", 
                    color="black", fontweight='bold', fontsize=9)
    ax5.set_title('各团队研发效能对比矩阵')
    cbar = plt.colorbar(im, ax=ax5, shrink=0.6)
    cbar.set_label('得分（1-5分）', fontsize=9)
    
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig('rd-effectiveness-dashboard.pdf', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: rd-effectiveness-dashboard.pdf")


def create_pdca():
    """PDCA循环图"""
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Draw outer circle
    circle = Circle((0, 0), 1.2, fill=False, edgecolor='#2c3e50', linewidth=3)
    ax.add_patch(circle)
    
    # Draw dividing lines
    ax.plot([0, 0], [-1.2, 1.2], 'k-', linewidth=2)
    ax.plot([-1.2, 1.2], [0, 0], 'k-', linewidth=2)
    
    # Add colored backgrounds for quadrants
    theta = np.linspace(0, 2*np.pi, 100)
    for r in [0.4, 0.7, 1.0]:
        # Plan (top-right)
        theta_q = np.linspace(0, np.pi/2, 25)
        ax.fill_between(np.cos(theta_q)*r, 0, np.sin(theta_q)*r, alpha=0.15, color='#3498db')
        # Do (top-left)
        theta_q = np.linspace(np.pi/2, np.pi, 25)
        ax.fill_between(np.cos(theta_q)*r, 0, np.sin(theta_q)*r, alpha=0.15, color='#2ecc71')
        # Check (bottom-left)
        theta_q = np.linspace(np.pi, 3*np.pi/2, 25)
        ax.fill_between(np.cos(theta_q)*r, 0, np.sin(theta_q)*r, alpha=0.15, color='#f39c12')
        # Act (bottom-right)
        theta_q = np.linspace(3*np.pi/2, 2*np.pi, 25)
        ax.fill_between(np.cos(theta_q)*r, 0, np.sin(theta_q)*r, alpha=0.15, color='#e74c3c')
    
    # 四阶段标签
    stages = [
        ('计划(P)\n识别差距\n设定目标', 0.6, 0.6, '#3498db'),
        ('执行(D)\n试点实施\n收集数据', -0.6, 0.6, '#2ecc71'),
        ('检查(C)\n效果评估\n差距分析', -0.6, -0.6, '#f39c12'),
        ('改进(A)\n标准化\n下一轮', 0.6, -0.6, '#e74c3c'),
    ]
    
    for label, x, y, color in stages:
        ax.text(x, y, label, ha='center', va='center', fontsize=10, 
                fontweight='bold', color=color)
    
    # 循环箭头
    for angle in [45, 135, 225, 315]:
        rad = np.radians(angle)
        x = 0.9 * np.cos(rad)
        y = 0.9 * np.sin(rad)
        dx = -0.15 * np.sin(rad)
        dy = 0.15 * np.cos(rad)
        ax.annotate('', xy=(x+dx, y+dy), xytext=(x, y),
                   arrowprops=dict(arrowstyle='->', color='#2c3e50', lw=2))
    
    # 中心文字
    ax.text(0, 0, '持续\n改进', ha='center', va='center', fontsize=14, 
            fontweight='bold', color='#2c3e50',
            bbox=dict(boxstyle='circle', facecolor='white', edgecolor='#2c3e50', linewidth=2))
    
    ax.text(0, 1.4, '百度研发管理PDCA持续改进循环', ha='center', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('pdca-improvement.pdf', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Generated: pdca-improvement.pdf")


if __name__ == '__main__':
    print("=" * 50)
    print("Generating Chapter 4 Figures...")
    print("=" * 50)
    
    create_org_evolution()
    create_swot_radar()
    create_amo_comparison()
    create_dual_channel()
    create_rd_dashboard()
    create_pdca()
    
    print("=" * 50)
    print("All figures generated successfully!")
    print("=" * 50)
