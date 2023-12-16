import pandas as pd
from scipy.stats import chi2_contingency, f_oneway

file_path = r"C:\Users\Tathagata\Downloads\208.csv"
df = pd.read_csv(file_path)

chi2, p, dof, expected = chi2_contingency(pd.crosstab(df['Area Code'], columns='count'))

print(f"Chi-square statistic: {chi2}")
print(f"P-value: {p}")

if p < 0.05:
    print("The distribution of cell towers across different Area codes is statistically significant.")
else:
    print("The distribution of cell towers across different Area codes is not statistically significant.")

anova_result = f_oneway(df['Longitude'], df['Latitude'], df['Range'], df['Number of Samples'])

print("\nANOVA Result:")
print(anova_result)

if anova_result.pvalue < 0.05:
    print("There are significant differences in the spatial distribution of cell towers between Area codes.")
else:
    print("There are no significant differences in the spatial distribution of cell towers between Area codes.")
