import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10

# 固定随机种子，保证可复现
np.random.seed(42)

# --------------------------
# 模拟数据（与原图趋势/分组完全对齐）
# --------------------------
treatments = ['Initial', 'D0', 'D1', 'D3', 'D6']

# 图a: SOM molecular richness
# Day 7 (前5组)
mol_day7 = [
    np.random.normal(10500, 800, 3),    # Initial
    np.random.normal(7200, 800, 3),     # D0
    np.random.normal(8500, 1200, 3),   # D1
    np.random.normal(10500, 500, 3),    # D3
    np.random.normal(10600, 400, 3)    # D6
]
# Day 90 (后4组)
mol_day90 = [
    np.random.normal(5200, 800, 3),     # D0
    np.random.normal(6300, 500, 3),     # D1
    np.random.normal(6800, 800, 3),     # D3
    np.random.normal(7000, 600, 3)      # D6
]
mol_all = mol_day7 + mol_day90
x_ticks_labels = ['Initial', 'D0', 'D1', 'D3', 'D6', 'D0', 'D1', 'D3', 'D6']

# 图b: Average ΔGcox
# Day 7 (前5组)
gcox_day7 = [
    np.random.normal(67.5, 0.3, 3),    # Initial
    np.random.normal(67.3, 0.4, 3),     # D0
    np.random.normal(66.5, 1.0, 3),     # D1
    np.random.normal(67.8, 0.3, 3),     # D3
    np.random.normal(68.2, 0.4, 3)      # D6
]
# Day 90 (后4组)
gcox_day90 = [
    np.random.normal(78.0, 0.3, 3),     # D0
    np.random.normal(77.3, 0.4, 3),     # D1
    np.random.normal(77.0, 0.3, 3),     # D3
    np.random.normal(78.0, 0.5, 3)      # D6
]
gcox_all = gcox_day7 + gcox_day90

# 配色：浅→深的橙/棕色渐变
colors = [
    '#888888', '#f0e6d6', '#f0c8a0', '#e69966', '#cc7033',
    '#f0e6d6', '#f0c8a0', '#e69966', '#cc7033'
]

# --------------------------
# 绘图（和原图1x2双列布局完全一致）
# --------------------------
fig, axes = plt.subplots(1, 2, figsize=(14, 6), dpi=100)

# --- 图a: SOM molecular richness ---
ax = axes[0]
bp = ax.boxplot(mol_all, patch_artist=True, widths=0.6, medianprops={'color':'black'})
# 设置箱体颜色
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.8)
# 添加均值点（白色圆点）
for i, data in enumerate(mol_all):
    mean_val = np.mean(data)
    ax.scatter(i+1, mean_val, color='white', edgecolor='black', zorder=3, s=40)

ax.set_xticks(range(1, len(x_ticks_labels)+1))
ax.set_xticklabels(x_ticks_labels)
ax.set_ylim(3000, 12500)
ax.set_ylabel('SOM molecular richness')
ax.set_xlabel('Treatment')
ax.text(0.05, 0.95, 'a', transform=ax.transAxes, fontsize=14, fontweight='bold')

# 添加Day7/Day90分组标注线
ax.plot([2, 5], [11500, 11500], color='black', linewidth=1)
ax.text(3.5, 11800, 'Day 7', ha='center', va='bottom')
ax.plot([6, 9], [8500, 8500], color='black', linewidth=1)
ax.text(7.5, 8800, 'Day 90', ha='center', va='bottom')

# --- 图b: Average ΔGcox ---
ax = axes[1]
bp = ax.boxplot(gcox_all, patch_artist=True, widths=0.6, medianprops={'color':'black'})
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.8)
# 添加均值点（白色圆点）
for i, data in enumerate(gcox_all):
    mean_val = np.mean(data)
    ax.scatter(i+1, mean_val, color='white', edgecolor='black', zorder=3, s=40)

ax.set_xticks(range(1, len(x_ticks_labels)+1))
ax.set_xticklabels(x_ticks_labels)
ax.set_ylim(62, 81)
ax.set_ylabel('Average $\Delta G^\\circ_{cox}$\n(kJ per mol C)')
ax.set_xlabel('Treatment')
ax.text(0.05, 0.95, 'b', transform=ax.transAxes, fontsize=14, fontweight='bold')

# 添加Day7/Day90分组标注线
ax.plot([2, 5], [70, 70], color='black', linewidth=1)
ax.text(3.5, 70.5, 'Day 7', ha='center', va='bottom')
ax.plot([6, 9], [80, 80], color='black', linewidth=1)
ax.text(7.5, 80.5, 'Day 90', ha='center', va='bottom')

plt.tight_layout()
plt.show()