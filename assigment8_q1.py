import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_stata('assignment8.dta')

bin_edges = np.arange(4.25, 5.65, 0.10)
bin_labels = [f'{edge:.2f}' for edge in bin_edges[:-1]]

def calculate_bin_percentages(data, bins):
    counts, _ = np.histogram(data, bins=bins)
    percentages = (counts / len(data)) * 100
    return percentages

feb_nj = df[(df['state'] == 1) & (df['time'] == 0)]['wage_st'].dropna()
feb_pa = df[(df['state'] == 0) & (df['time'] == 0)]['wage_st'].dropna()
nov_nj = df[(df['state'] == 1) & (df['time'] == 1)]['wage_st'].dropna()
nov_pa = df[(df['state'] == 0) & (df['time'] == 1)]['wage_st'].dropna()

feb_nj_pct = calculate_bin_percentages(feb_nj, bin_edges)
feb_pa_pct = calculate_bin_percentages(feb_pa, bin_edges)
nov_nj_pct = calculate_bin_percentages(nov_nj, bin_edges)
nov_pa_pct = calculate_bin_percentages(nov_pa, bin_edges)

x = np.arange(len(bin_labels))
width = 0.40  

# FIGURE 1:
fig1, ax1 = plt.subplots(figsize=(10, 5))

bars1 = ax1.bar(x - width/2, feb_nj_pct, width, label='New Jersey', 
                color='black', edgecolor='black', linewidth=0.5)
bars2 = ax1.bar(x + width/2, feb_pa_pct, width, label='Pennsylvania',
                color='white', edgecolor='black', linewidth=0.5, 
                hatch='////')  

ax1.set_xlabel('Wage Range', fontsize=10)
ax1.set_ylabel('Percent of Stores', fontsize=10)
ax1.set_title('February 1992', fontsize=11, fontweight='bold', loc='left')
ax1.set_xticks(x)
ax1.set_xticklabels(bin_labels, rotation=0, ha='center', fontsize=9)
ax1.set_ylim(0, 40)
ax1.set_yticks(np.arange(0, 45, 10))
ax1.legend(fontsize=9, loc='upper right', frameon=False)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.savefig('figure1_feb1992.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()

# FIGURE 2: 
fig2, ax2 = plt.subplots(figsize=(10, 5))

bars3 = ax2.bar(x - width/2, nov_nj_pct, width, label='New Jersey',
                color='black', edgecolor='black', linewidth=0.5)
bars4 = ax2.bar(x + width/2, nov_pa_pct, width, label='Pennsylvania',
                color='white', edgecolor='black', linewidth=0.5,
                hatch='////')

ax2.set_xlabel('Wage Range', fontsize=10)
ax2.set_ylabel('Percent of Stores', fontsize=10)
ax2.set_title('November 1992', fontsize=11, fontweight='bold', loc='left')
ax2.set_xticks(x)
ax2.set_xticklabels(bin_labels, rotation=0, ha='center', fontsize=9)
ax2.set_ylim(0, 90)
ax2.set_yticks(np.arange(0, 100, 10))
ax2.legend(fontsize=9, loc='upper right', frameon=False)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.savefig('figure1_nov1992.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()

print("Figures saved as 'figure1_feb1992.png' and 'figure1_nov1992.png'")
