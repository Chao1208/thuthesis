#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成第四章（百度案例研究）所需的所有图表
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, FancyArrowPatch, Wedge
import numpy as np
from matplotlib import rcParams

# 设置中文字体
rcParams['font.family'] = ['SimHei', 'DejaVu Sans']
rcParams['axes.unicode_minus'] = False

# 设置更大的字体
plt.rcParams['font.size'] = 11
plt.rcParams['axes.titlesize'] = 13
plt.rcParams['axes.labelsize'] = 11

def create_org_evolution():
    """图1: 百度研发组织架构演变图"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))
    
    # 左图: 烟囱式架构（调整前）
    ax1 = axes[0]
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title('(a) 调整前：烟囱式架构', fontsize=14, fontweight='bold', pad=20)
    
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
    
    # 绘制复杂的连接线表示壁垒
    for i in range(len(departments)):
        for j in range(i+1, len(departments)):
            x1 = 1 + (i % 4) * 2
            y1 = 7 - (i // 4) * 3
            x2 = 1 + (j % 4) * 2
            y2 = 7 - (j // 4) * 3
            if abs(x1-x2) <= 2 and abs(y1-y2) <= 3:
                ax1.plot([x1, x2], [y1, y2], 'r--', alpha=0.2, linewidth=0.5)
    
    # 添加问题标注
    ax1.annotate('部门墙\n沟通壁垒', xy=(5, 9), fontsize=10, ha='center', 
                color='red', fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
    
    # 右图: BMU/AMU架构（调整后）
    ax2 = axes[1]
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title('(b) 调整后：BMU/AMU双BU架构', fontsize=14, fontweight='bold', pad=20)
    
    # 绘制BMU
    bmu_rect = FancyBboxPatch((1, 5.5), 3.5, 3, boxstyle="round,pad=0.15",
                              facecolor='#3498db', edgecolor='#2c3e50', linewidth=2)
    ax2.add_patch(bmu_rect)
    ax2.text(2.75, 7.5, 'BMU', ha='center', va='center', fontsize=13, 
             fontweight='bold', color='white')
    ax2.text(2.75, 6.8, '基础模型与理解', ha='center', va='center', fontsize=9, color='white')
    ax2.text(2.75, 6.2, '文心大模型 | 飞桨', ha='center', va='center', fontsize=8, color='white')
    
    # 绘制AMU
    amu_rect = FancyBboxPatch((5.5, 5.5), 3.5, 3, boxstyle="round,pad=0.15",
                              facecolor='#e74c3c', edgecolor='#2c3e50', linewidth=2)
    ax2.add_patch(amu_rect)
    ax2.text(7.25, 7.5, 'AMU', ha='center', va='center', fontsize=13, 
             fontweight='bold', color='white')
    ax2.text(7.25, 6.8, '应用与多模态', ha='center', va='center', fontsize=9, color='white')
    ax2.text(7.25, 6.2, '行业应用 | 场景落地', ha='center', va='center', fontsize=8, color='white')
    
    # 绘制平台层
    platform_rect = FancyBboxPatch((2.5, 3), 5, 1.5, boxstyle="round,pad=0.1",
                                   facecolor='#2ecc71', edgecolor='#27ae60', linewidth=2)
    ax2.add_patch(platform_rect)
    ax2.text(5, 3.75, '共性平台层：飞桨 | 百度大脑 | AI中台', 
             ha='center', va='center', fontsize=10, fontweight='bold', color='white')
    
    # 绘制业务场景层
    scenarios = ['搜索', '智能云', 'Apollo', '智能设备']
    for i, scenario in enumerate(scenarios):
        x = 1.5 + i * 2
        rect = FancyBboxPatch((x-0.7, 0.8), 1.4, 1.2, boxstyle="round,pad=0.08",
                              facecolor='#f39c12', edgecolor='#d68910', linewidth=1.5)
        ax2.add_patch(rect)
        ax2.text(x, 1.4, scenario, ha='center', va='center', fontsize=9, fontweight='bold')
    
    # 添加连接箭头
    ax2.annotate('', xy=(5, 5.5), xytext=(5, 4.5),
                arrowprops=dict(arrowstyle='<->', color='#34495e', lw=2))
    ax2.annotate('', xy=(5, 3), xytext=(5, 2),
                arrowprops=dict(arrowstyle='<->', color='#34495e', lw=2))
    
    # 添加协同标注
    ax2.annotate('统一规划\n协同高效', xy=(5, 9), fontsize=10, ha='center', 
                color='green', fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    
    plt.tight_layout()
    plt.savefig('baidu-org-evolution.pdf', dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig('baidu-org-evolution.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 生成图表: baidu-org-evolution.pdf")


def create_swot_radar():
    """图2: SWOT战略四象限雷达图"""
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))
    
    # 数据
    categories = ['SO\n(优势-机会)', 'WO\n(劣势-机会)', 'WT\n(劣势-威胁)', 'ST\n(优势-威胁)']
    N = len(categories)
    
    # 百度得分
    baidu_scores = [4.15, 3.85, 2.10, 2.40]
    # 行业平均
    industry_avg = [3.50, 3.20, 2.80, 2.60]
    # 标杆企业（字节跳动）
    benchmark = [4.30, 3.60, 2.40, 2.80]
    
    # 计算角度
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]  # 闭合图形
    
    # 数据闭合
    baidu_scores += baidu_scores[:1]
    industry_avg += industry_avg[:1]
    benchmark += benchmark[:1]
    
    # 绘制
    ax.plot(angles, baidu_scores, 'o-', linewidth=2.5, label='百度', color='#e74c3c')
    ax.fill(angles, baidu_scores, alpha=0.25, color='#e74c3c')
    
    ax.plot(angles, industry_avg, 's--', linewidth=2, label='行业平均', color='#95a5a6')
    ax.fill(angles, industry_avg, alpha=0.15, color='#95a5a6')
    
    ax.plot(angles, benchmark, '^:', linewidth=2, label='标杆企业', color='#3498db')
    ax.fill(angles, benchmark, alpha=0.15, color='#3498db')
    
    # 设置标签
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=11)
    ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(['1', '2', '3', '4', '5'], fontsize=9)
    
    ax.set_title('百度研发管理SWOT战略四象限分析', fontsize=14, fontweight='bold', pad=20)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.savefig('swot-radar-baidu.pdf', dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig('swot-radar-baidu.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 生成图表: swot-radar-baidu.pdf")


def create_amo_comparison():
    """图3: AMO三维对比图"""
    fig = plt.figure(figsize=(12, 5))
    
    # 左图: 3D柱状图
    ax1 = fig.add_subplot(121, projection='3d')
    
    companies = ['百度', '阿里巴巴', '腾讯', '字节跳动', '行业平均']
    dimensions = ['能力(A)', '动机(M)', '机会(O)']
    
    # 数据 (1-5分)
    data = np.array([
        [3.8, 3.2, 3.5],  # 百度
        [4.0, 3.8, 3.8],  # 阿里
        [3.9, 3.6, 3.7],  # 腾讯
        [4.2, 4.0, 4.1],  # 字节
        [3.5, 3.4, 3.5],  # 行业平均
    ])
    
    xpos = np.arange(len(companies))
    ypos = np.arange(len(dimensions))
    xpos, ypos = np.meshgrid(xpos, ypos)
    xpos = xpos.flatten()
    ypos = ypos.flatten()
    zpos = np.zeros_like(xpos)
    
    dx = dy = 0.5
    dz = data.flatten()
    
    colors = ['#e74c3c' if i == 0 else '#3498db' if i == 3 else '#95a5a6' 
              for i in xpos]
    
    ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors, alpha=0.8)
    
    ax1.set_xticks(np.arange(len(companies)) + dx/2)
    ax1.set_xticklabels(companies, fontsize=9)
    ax1.set_yticks(np.arange(len(dimensions)) + dy/2)
    ax1.set_yticklabels(dimensions, fontsize=9)
    ax1.set_zlabel('得分', fontsize=10)
    ax1.set_title('AMO三维度企业对比', fontsize=12, fontweight='bold')
    ax1.set_zlim(0, 5)
    
    # 右图: 热力图对比
    ax2 = fig.add_subplot(122)
    
    im = ax2.imshow(data.T, cmap='RdYlGn', aspect='auto', vmin=2.5, vmax=4.5)
    
    ax2.set_xticks(np.arange(len(companies)))
    ax2.set_yticks(np.arange(len(dimensions)))
    ax2.set_xticklabels(companies, fontsize=10)
    ax2.set_yticklabels(dimensions, fontsize=10)
    
    # 添加数值标注
    for i in range(len(companies)):
        for j in range(len(dimensions)):
            text = ax2.text(i, j, f'{data[i, j]:.1f}',
                           ha="center", va="center", color="black", fontweight='bold', fontsize=11)
    
    ax2.set_title('AMO维度得分热力图', fontsize=12, fontweight='bold')
    
    # 添加颜色条
    cbar = plt.colorbar(im, ax=ax2, shrink=0.8)
    cbar.set_label('得分', fontsize=10)
    
    # 添加图例说明
    fig.text(0.5, 0.02, '红色=百度  蓝色=字节跳动(标杆)  灰色=其他', 
             ha='center', fontsize=10, style='italic')
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.97])
    plt.savefig('amo-comparison.pdf', dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig('amo-comparison.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 生成图表: amo-comparison.pdf")


def create_dual_career_channel():
    """图4: 双通道职业发展体系"""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # 标题
    ax.text(5, 9.5, '百度研发人员双通道职业发展体系', fontsize=15, 
            ha='center', fontweight='bold')
    
    # 管理通道（左侧）
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
        ax.text(2.5, y, label, ha='center', va='center', fontsize=10, 
                color='white' if y > 5 else 'black', fontweight='bold')
    
    # 技术通道（右侧）
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
        ax.text(7.5, y, label, ha='center', va='center', fontsize=10, 
                color='white' if y > 5 else 'black', fontweight='bold')
    
    # 添加通道标签
    ax.text(2.5, 1.0, '管理通道', ha='center', fontsize=13, fontweight='bold', color='#2c3e50')
    ax.text(7.5, 1.0, '技术通道', ha='center', fontsize=13, fontweight='bold', color='#8e44ad')
    
    # 添加横向流动箭头
    for y in [2.0, 3.3, 4.6]:
        ax.annotate('', xy=(5.9, y), xytext=(4.1, y),
                   arrowprops=dict(arrowstyle='<->', color='#e67e22', lw=2))
    
    ax.text(5, 1.6, '双向流动通道', ha='center', fontsize=10, color='#e67e22', fontweight='bold')
    
    # 添加底部说明
    ax.text(5, 0.3, '注：两通道在总监/科学家级别以上薪酬待遇对等，晋升周期2-3年/级',
            ha='center', fontsize=9, style='italic', color='#666666')
    
    plt.tight_layout()
    plt.savefig('dual-career-channel.pdf', dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig('dual-career-channel.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 生成图表: dual-career-channel.pdf")


def create_rd_dashboard():
    """图5: 研发效能仪表盘"""
    fig = plt.figure(figsize=(14, 8))
    
    # 创建子图布局
    gs = fig.add_gridspec(3, 4, hspace=0.4, wspace=0.3)
    
    # 1. 交付效率指标（左上）
    ax1 = fig.add_subplot(gs[0, :2])
    metrics1 = ['需求交付\n周期', '迭代完成率', '发布频率', '代码提交量']
    values1 = [8.5, 88, 2.1, 1250]  # 当前值
    targets1 = [10, 90, 2.5, 1500]   # 目标值
    
    x = np.arange(len(metrics1))
    width = 0.35
    
    bars1 = ax1.bar(x - width/2, values1, width, label='当前', color='#3498db', alpha=0.8)
    bars2 = ax1.bar(x + width/2, targets1, width, label='目标', color='#e74c3c', alpha=0.6)
    
    ax1.set_ylabel('数值', fontsize=10)
    ax1.set_title('交付效率指标', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(metrics1, fontsize=9)
    ax1.legend(fontsize=9)
    ax1.grid(axis='y', alpha=0.3)
    
    # 2. 质量指标（右上）
    ax2 = fig.add_subplot(gs[0, 2:])
    metrics2 = ['线上故障', '代码评审\n通过率', '测试覆盖率', 'TD密度']
    values2 = [12, 94, 78, 0.35]
    
    colors2 = ['#e74c3c' if v > 10 else '#2ecc71' if v > 90 else '#f39c12' for v in values2]
    
    bars = ax2.bar(metrics2, values2, color=colors2, alpha=0.8, edgecolor='black')
    ax2.set_ylabel('数值', fontsize=10)
    ax2.set_title('质量指标', fontsize=12, fontweight='bold')
    ax2.set_xticklabels(metrics2, fontsize=9)
    ax2.grid(axis='y', alpha=0.3)
    
    # 添加阈值线
    ax2.axhline(y=10, color='green', linestyle='--', alpha=0.5, label='目标线')
    
    # 3. 趋势图（左中，跨两列）
    ax3 = fig.add_subplot(gs[1, :2])
    months = ['1月', '2月', '3月', '4月', '5月', '6月']
    efficiency_trend = [2.4, 2.5, 2.6, 2.5, 2.7, 2.65]
    quality_trend = [3.2, 3.3, 3.1, 3.4, 3.5, 3.45]
    
    ax3.plot(months, efficiency_trend, 'o-', label='交付效率指数', linewidth=2, color='#3498db')
    ax3.plot(months, quality_trend, 's-', label='质量指数', linewidth=2, color='#2ecc71')
    ax3.set_ylabel('指数值', fontsize=10)
    ax3.set_title('研发效能趋势（近6个月）', fontsize=12, fontweight='bold')
    ax3.legend(fontsize=9)
    ax3.grid(True, alpha=0.3)
    
    # 4. 饼图 - 资源分配（右中）
    ax4 = fig.add_subplot(gs[1, 2:])
    labels = ['新功能开发', 'TD偿还', '技术预研', '运营支持']
    sizes = [55, 20, 15, 10]
    colors4 = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']
    explode = (0, 0.05, 0, 0)
    
    ax4.pie(sizes, explode=explode, labels=labels, colors=colors4, autopct='%1.0f%%',
            shadow=True, startangle=90, textprops={'fontsize': 9})
    ax4.set_title('研发资源分配', fontsize=12, fontweight='bold')
    
    # 5. 热力图 - 团队对比（底部，跨全部）
    ax5 = fig.add_subplot(gs[2, :])
    teams = ['搜索团队', '推荐团队', '云团队', 'Apollo', '大模型']
    indicators = ['交付效率', '代码质量', '创新产出', '协作效率', 'TD控制']
    
    # 生成热力图数据
    heatmap_data = np.array([
        [4.2, 4.0, 3.5, 3.8, 3.2],  # 搜索
        [3.8, 3.5, 4.0, 3.5, 3.0],  # 推荐
        [3.5, 4.2, 3.8, 3.2, 4.0],  # 云
        [3.2, 3.8, 4.5, 3.0, 3.5],  # Apollo
        [4.0, 3.5, 4.8, 3.8, 2.8],  # 大模型
    ])
    
    im = ax5.imshow(heatmap_data, cmap='RdYlGn', aspect='auto', vmin=2, vmax=5)
    
    ax5.set_xticks(np.arange(len(indicators)))
    ax5.set_yticks(np.arange(len(teams)))
    ax5.set_xticklabels(indicators, fontsize=10)
    ax5.set_yticklabels(teams, fontsize=10)
    
    # 添加数值标注
    for i in range(len(teams)):
        for j in range(len(indicators)):
            text = ax5.text(j, i, f'{heatmap_data[i, j]:.1f}',
                           ha="center", va="center", color="black", fontweight='bold', fontsize=10)
    
    ax5.set_title('各团队研发效能对比矩阵', fontsize=12, fontweight='bold', pad=10)
    
    # 添加颜色条
    cbar = plt.colorbar(im, ax=ax5, orientation='horizontal', pad=0.15, shrink=0.6)
    cbar.set_label('得分 (1-5分)', fontsize=9)
    
    plt.suptitle('百度研发效能综合仪表盘', fontsize=16, fontweight='bold', y=0.98)
    
    plt.savefig('rd-effectiveness-dashboard.pdf', dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig('rd-effectiveness-dashboard.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 生成图表: rd-effectiveness-dashboard.pdf")


def create_pdca_cycle():
    """图6: PDCA持续改进循环"""
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # 绘制四个象限
    theta = np.linspace(0, 2*np.pi, 100)
    
    # Plan - 右上 (0-90度)
    theta_plan = np.linspace(np.pi/2, 0, 50)
    for r in [0.3, 0.6, 0.9, 1.2]:
        ax.fill_between(np.cos(theta_plan)*r, 0, np.sin(theta_plan)*r, 
                       alpha=0.1, color='#3498db')
    
    # Do - 左上 (90-180度)
    theta_do = np.linspace(np.pi, np.pi/2, 50)
    for r in [0.3, 0.6, 0.9, 1.2]:
        ax.fill_between(np.cos(theta_do)*r, 0, np.sin(theta_do)*r, 
                       alpha=0.1, color='#2ecc71')
    
    # Check - 左下 (180-270度)
    theta_check = np.linspace(3*np.pi/2, np.pi, 50)
    for r in [0.3, 0.6, 0.9, 1.2]:
        ax.fill_between(np.cos(theta_check)*r, 0, np.sin(theta_check)*r, 
                       alpha=0.1, color='#f39c12')
    
    # Act - 右下 (270-360度)
    theta_act = np.linspace(2*np.pi, 3*np.pi/2, 50)
    for r in [0.3, 0.6, 0.9, 1.2]:
        ax.fill_between(np.cos(theta_act)*r, 0, np.sin(theta_act)*r, 
                       alpha=0.1, color='#e74c3c')
    
    # 绘制外圆
    circle = Circle((0, 0), 1.2, fill=False, edgecolor='#2c3e50', linewidth=3)
    ax.add_patch(circle)
    
    # 绘制分隔线
    ax.plot([0, 0], [-1.2, 1.2], 'k-', linewidth=2)
    ax.plot([-1.2, 1.2], [0, 0], 'k-', linewidth=2)
    
    # 添加阶段标签
    stages = [
        ('Plan\n(计划)', 0.6, 0.6, '#3498db',
         '• 识别改进机会\n• 制定改进目标\n• 设计改进方案'),
        ('Do\n(执行)', -0.6, 0.6, '#2ecc71',
         '• 试点实施\n• 数据收集\n• 过程监控'),
        ('Check\n(检查)', -0.6, -0.6, '#f39c12',
         '• 效果评估\n• 差距分析\n• 经验总结'),
        ('Act\n(改进)', 0.6, -0.6, '#e74c3c',
         '• 标准化推广\n• 制度固化\n• 新一轮PDCA'),
    ]
    
    for label, x, y, color, desc in stages:
        # 阶段标题
        ax.text(x, y, label, ha='center', va='center', fontsize=14, 
                fontweight='bold', color=color)
        # 详细内容
        ax.text(x, y-0.35, desc, ha='center', va='top', fontsize=9, color='#333333')
    
    # 添加箭头表示循环
    arrow_style = "Simple, tail_width=6, head_width=12, head_length=8"
    kw = dict(arrowstyle=arrow_style, color="#2c3e50")
    
    # 顺时针箭头
    for angle in [45, 135, 225, 315]:
        rad = np.radians(angle)
        x = 0.9 * np.cos(rad)
        y = 0.9 * np.sin(rad)
        dx = -0.2 * np.sin(rad)
        dy = 0.2 * np.cos(rad)
        ax.annotate('', xy=(x+dx, y+dy), xytext=(x, y),
                   arrowprops=dict(arrowstyle='->', color='#2c3e50', lw=2))
    
    # 中心文字
    ax.text(0, 0, '持续\n改进', ha='center', va='center', fontsize=16, 
            fontweight='bold', color='#2c3e50',
            bbox=dict(boxstyle='circle', facecolor='white', edgecolor='#2c3e50', linewidth=2))
    
    # 标题
    ax.text(0, 1.4, '百度研发管理PDCA持续改进循环', ha='center', fontsize=15, fontweight='bold')
    
    # 底部说明
    ax.text(0, -1.4, '循环周期：月度检视 | 季度复盘 | 年度战略回顾', 
            ha='center', fontsize=10, style='italic', color='#666666')
    
    plt.tight_layout()
    plt.savefig('pdca-improvement.pdf', dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig('pdca-improvement.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 生成图表: pdca-improvement.pdf")


if __name__ == '__main__':
    print("=" * 50)
    print("开始生成第四章图表...")
    print("=" * 50)
    
    create_org_evolution()
    create_swot_radar()
    create_amo_comparison()
    create_dual_career_channel()
    create_rd_dashboard()
    create_pdca_cycle()
    
    print("=" * 50)
    print("所有图表生成完成！")
    print("=" * 50)
