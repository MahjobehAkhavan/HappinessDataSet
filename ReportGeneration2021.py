import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('world-happiness-report-2021.csv')

# extract all regions in dataset
unique_region = df['Regional indicator'].unique()

regions = []
mean_values = []
for region in unique_region:
    regions.append(region)
    mean = df[df['Regional indicator'] == region]['Ladder score'].mean()
    mean_values.append(mean)

plt.bar(regions, mean_values, color='royalblue', alpha=0.7)
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
plt.xlabel('Regions')
plt.ylabel('Ladder Score')
plt.title('Regional Happiness')
plt.xticks(rotation=45, horizontalalignment='right', fontweight='light', fontsize='medium')
plt.tight_layout()
# plt.show()
plt.savefig('Regional Happiness.png')
print('*')