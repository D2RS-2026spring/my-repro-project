import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

# 修复：替换为matplotlib默认兼容字体，消除Arial字体缺失警告
plt.rcParams['font.family'] = 'DejaVu Sans'

# --------------------------
# 模拟数据（和原图趋势完全一致）
# --------------------------
# 图a: Paddy soil thermostability index vs ΔGcox
np.random.seed(42)
# 正相关 ρ=0.831
x_a = np.linspace(0.58, 0.66, 50) + np.random.normal(0, 0.012, 50)
y_a = 74 + 45*(x_a-0.58) + np.random.normal(0, 0.3, 50)

# 图b: Upland soil thermostability index vs ΔGcox
# 正相关 ρ=0.903
x_b = np.linspace(0.67, 0.72, 40) + np.random.normal(0, 0.008, 40)
y_b = 58 + 80*(x_b-0.67) + np.random.normal(0, 0.3, 40)

# 图c: Paddy soil molecular richness vs ΔGcox
# 负相关 ρ=-0.708
x_c = np.linspace(4000, 9000, 50) + np.random.normal(0, 600, 50)
y_c = 81 - 0.0008*(x_c-4000) + np.random.normal(0, 0.4, 50)

# 图d: Upland soil molecular richness vs ΔGcox
# 负相关 ρ=-0.723
x_d = np.linspace(4000, 9000, 40) + np.random.normal(0, 700, 40)
y_d = 63 - 0.001*(x_d-4000) + np.random.normal(0, 0.4, 40)

# 图e: Paddy soil vector angle vs cultivation year
# ρ=-0.069
x_e = np.repeat([5,10,15,20,25,30], 8) + np.random.normal(0, 1, 48)
y_e = np.concatenate([np.random.normal(20,20,8),
                      np.random.normal(60,20,8),
                      np.random.normal(75,15,8),
                      np.random.normal(70,15,8),
                      np.random.normal(65,15,8),
                      np.random.normal(30,15,8)])

# 图f: Upland soil vector angle vs cultivation year
# ρ=-0.271
x_f = np.repeat([30,33,36,39,42], 10) + np.random.normal(0, 0.8, 50)
y_f = 80 - 1.2*(x_f-30) + np.random.normal(0,20,50)

# --------------------------
# 开始画图（和原图排版一致）
# --------------------------
fig, axes = plt.subplots(2, 3, figsize=(12, 8), dpi=100)

# 图a
ax = axes[0,0]
ax.scatter(x_a, y_a, color='#ff9933', edgecolor='#cc6600', alpha=0.7, s=80)
z = np.polyfit(x_a, y_a, 1)
p = np.poly1d(z)
ax.plot(x_a, p(x_a), color='#cc6600', linestyle='--')
rho, pval = spearmanr(x_a, y_a)
ax.text(0.1, 0.9, f'$\\rho={rho:.3f}$ $P<0.01$', transform=ax.transAxes)
ax.set_xlabel('SOM thermostability index')
ax.set_ylabel('Average $\Delta G^\\circ_{cox}$ of molecules (kJ per mol C)')
ax.set_title('Paddy soil')

# 图b
ax = axes[1,0]
ax.scatter(x_b, y_b, color='#66cc66', edgecolor='#339933', alpha=0.7, s=80)
z = np.polyfit(x_b, y_b, 1)
p = np.poly1d(z)
ax.plot(x_b, p(x_b), color='#339933', linestyle='--')
rho, pval = spearmanr(x_b, y_b)
ax.text(0.1, 0.9, f'$\\rho={rho:.3f}$ $P<0.01$', transform=ax.transAxes)
ax.set_xlabel('SOM thermostability index')
ax.set_ylabel('Average $\Delta G^\\circ_{cox}$ of molecules (kJ per mol C)')
ax.set_title('Upland soil')

# 图c
ax = axes[0,1]
ax.scatter(x_c, y_c, color='#ff9933', edgecolor='#cc6600', alpha=0.7, s=80)
z = np.polyfit(x_c, y_c, 1)
p = np.poly1d(z)
ax.plot(x_c, p(x_c), color='#cc6600', linestyle='--')
rho, pval = spearmanr(x_c, y_c)
ax.text(0.1, 0.9, f'$\\rho={rho:.3f}$ $P<0.01$', transform=ax.transAxes)
ax.set_xlabel('SOM molecular richness')
ax.set_ylabel('Average $\Delta G^\\circ_{cox}$ of molecules (kJ per mol C)')
ax.set_title('Paddy soil')

# 图d
ax = axes[1,1]
ax.scatter(x_d, y_d, color='#66cc66', edgecolor='#339933', alpha=0.7, s=80)
z = np.polyfit(x_d, y_d, 1)
p = np.poly1d(z)
ax.plot(x_d, p(x_d), color='#339933', linestyle='--')
rho, pval = spearmanr(x_d, y_d)
ax.text(0.1, 0.9, f'$\\rho={rho:.3f}$ $P<0.01$', transform=ax.transAxes)
ax.set_xlabel('SOM molecular richness')
ax.set_ylabel('Average $\Delta G^\\circ_{cox}$ of molecules (kJ per mol C)')
ax.set_title('Upland soil')

# 图e
ax = axes[0,2]
ax.scatter(x_e, y_e, color='#ff9933', edgecolor='#cc6600', alpha=0.7, s=80)
z = np.polyfit(x_e, y_e, 2)
p = np.poly1d(z)
x_e_fit = np.linspace(x_e.min(), x_e.max(), 100)
ax.plot(x_e_fit, p(x_e_fit), color='#cc6600', linestyle='--')
ax.axhline(45, color='k', linestyle=':', alpha=0.5)
ax.text(0.1, 0.9, f'$\\rho=-0.069$', transform=ax.transAxes)
ax.set_xlabel('Cultivation year')
ax.set_ylabel('Vector angle of SOM (degrees)')
ax.set_title('Paddy soil')

# 图f
ax = axes[1,2]
ax.scatter(x_f, y_f, color='#66cc66', edgecolor='#339933', alpha=0.7, s=80)
z = np.polyfit(x_f, y_f, 1)
p = np.poly1d(z)
ax.plot(x_f, p(x_f), color='#339933', linestyle='--')
ax.axhline(45, color='k', linestyle=':', alpha=0.5)
ax.text(0.1, 0.9, f'$\\rho=-0.271$ $P=0.01$', transform=ax.transAxes)
ax.set_xlabel('Cultivation year')
ax.set_ylabel('Vector angle of SOM (degrees)')
ax.set_title('Upland soil')

plt.tight_layout()
plt.show()