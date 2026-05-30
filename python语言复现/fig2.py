import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10

# --------------------------
# 模拟数据（和原图趋势/分组一致）
# --------------------------
# 耕作年份与分组标签
paddy_treatments = ['Initial', 'Control', 'OM', 'NPK', 'NPKM']
upland_treatments = ['Control', 'OM', 'NPK', 'NPKM']
paddy_years = ['Y0', 'Y8', 'Y14', 'Y18', 'Y21', 'Y26', 'Y31']
upland_years = ['Y29', 'Y32', 'Y35', 'Y38', 'Y41']

# 稻田数据（分子多样性、ΔGcox、热稳定性指数）
np.random.seed(42)
# 分子多样性
paddy_div = [
    np.random.normal(4500, 300, 3),          # Initial
    np.random.normal(7000, 800, 3*4),         # Control
    np.random.normal(7500, 1000, 3*4),        # OM
    np.random.normal(8000, 1200, 3*4),        # NPK
    np.random.normal(7500, 1000, 3*4)         # NPKM
]
# ΔGcox
paddy_gcox = [
    np.random.normal(78, 0.5, 3),             # Initial
    np.random.normal(76, 1, 3*4),             # Control
    np.random.normal(76.5, 1, 3*4),           # OM
    np.random.normal(77, 1.2, 3*4),           # NPK
    np.random.normal(77.5, 1, 3*4)            # NPKM
]
# 热稳定性指数
paddy_thermo = [
    np.random.normal(0.64, 0.01, 3),          # Initial
    np.random.normal(0.635, 0.015, 3*4),      # Control
    np.random.normal(0.638, 0.015, 3*4),      # OM
    np.random.normal(0.632, 0.02, 3*4),       # NPK
    np.random.normal(0.635, 0.015, 3*4)      # NPKM
]

# 旱地数据（分子多样性、ΔGcox、热稳定性指数）
upland_div = [
    np.random.normal(5000, 1000, 3*4),        # Control
    np.random.normal(6000, 1200, 3*4),        # OM
    np.random.normal(7000, 1000, 3*4),        # NPK
    np.random.normal(6000, 800, 3*4)          # NPKM
]
upland_gcox = [
    np.random.normal(62, 1, 3*4),             # Control
    np.random.normal(62.5, 1, 3*4),           # OM
    np.random.normal(60.5, 1, 3*4),           # NPK
    np.random.normal(61, 1, 3*4)              # NPKM
]
upland_thermo = [
    np.random.normal(0.70, 0.015, 3*4),      # Control
    np.random.normal(0.705, 0.015, 3*4),      # OM
    np.random.normal(0.685, 0.015, 3*4),      # NPK
    np.random.normal(0.69, 0.015, 3*4)        # NPKM
]

# 配色（稻田黄橙红系，旱地绿色系）
paddy_colors = ['#888888', '#f9d057', '#f29e4e', '#e66b5b', '#d1495b']
upland_colors = ['#a5d6a7', '#81c784', '#66bb6a', '#43a047']

# --------------------------
# 绘图（和原图排版完全一致：左列稻田，右列旱地）
# --------------------------
fig, axes = plt.subplots(3, 2, figsize=(14, 10), dpi=100)

# --------------------------
# 左列：稻田土壤
# --------------------------
# 图1：分子多样性
ax = axes[0,0]
bp = ax.boxplot(paddy_div, patch_artist=True, positions=range(len(paddy_treatments)), widths=0.6)
for patch, color in zip(bp['boxes'], paddy_colors):
    patch.set_facecolor(color)
ax.set_xticks(range(len(paddy_treatments)))
ax.set_xticklabels(paddy_treatments)
ax.set_ylim(3500, 9500)
ax.set_ylabel('Molecular diversity')
ax.set_title('Paddy soil')

# 图2：ΔGcox
ax = axes[1,0]
bp = ax.boxplot(paddy_gcox, patch_artist=True, positions=range(len(paddy_treatments)), widths=0.6)
for patch, color in zip(bp['boxes'], paddy_colors):
    patch.set_facecolor(color)
ax.set_xticks(range(len(paddy_treatments)))
ax.set_xticklabels(paddy_treatments)
ax.set_ylim(73, 81)
ax.set_ylabel('Average $\Delta G^\\circ_{cox}$\n(kJ per mol C)')

# 图3：热稳定性指数
ax = axes[2,0]
bp = ax.boxplot(paddy_thermo, patch_artist=True, positions=range(len(paddy_treatments)), widths=0.6)
for patch, color in zip(bp['boxes'], paddy_colors):
    patch.set_facecolor(color)
ax.set_xticks(range(len(paddy_treatments)))
ax.set_xticklabels(paddy_treatments)
ax.set_ylim(0.59, 0.73)
ax.set_ylabel('Thermostability index')
ax.set_xlabel('Cultivation years')

# --------------------------
# 右列：旱地土壤
# --------------------------
# 图1：分子多样性
ax = axes[0,1]
bp = ax.boxplot(upland_div, patch_artist=True, positions=range(len(upland_treatments)), widths=0.6)
for patch, color in zip(bp['boxes'], upland_colors):
    patch.set_facecolor(color)
ax.set_xticks(range(len(upland_treatments)))
ax.set_xticklabels(upland_treatments)
ax.set_ylim(3500, 9500)
ax.set_title('Upland soil')

# 图2：ΔGcox
ax = axes[1,1]
bp = ax.boxplot(upland_gcox, patch_artist=True, positions=range(len(upland_treatments)), widths=0.6)
for patch, color in zip(bp['boxes'], upland_colors):
    patch.set_facecolor(color)
ax.set_xticks(range(len(upland_treatments)))
ax.set_xticklabels(upland_treatments)
ax.set_ylim(58, 64)
ax.set_ylabel('Average $\Delta G^\\circ_{cox}$\n(kJ per mol C)')

# 图3：热稳定性指数
ax = axes[2,1]
bp = ax.boxplot(upland_thermo, patch_artist=True, positions=range(len(upland_treatments)), widths=0.6)
for patch, color in zip(bp['boxes'], upland_colors):
    patch.set_facecolor(color)
ax.set_xticks(range(len(upland_treatments)))
ax.set_xticklabels(upland_treatments)
ax.set_ylim(0.53, 0.73)
ax.set_ylabel('Thermostability index')

plt.tight_layout()
plt.show()