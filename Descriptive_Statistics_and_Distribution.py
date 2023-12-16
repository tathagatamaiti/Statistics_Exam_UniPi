import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = r"C:\Users\Tathagata\Downloads\208.csv"
df = pd.read_csv(file_path)

mean_values = df[['Longitude', 'Latitude', 'Range', 'Number of Samples']].mean()
median_values = df[['Longitude', 'Latitude', 'Range', 'Number of Samples']].median()

print("Mean values:")
print(mean_values)

print("\nMedian values:")
print(median_values)

std_deviation_values = df[['Longitude', 'Latitude', 'Range', 'Number of Samples']].std()
variance_values = df[['Longitude', 'Latitude', 'Range', 'Number of Samples']].var()

print("\nStandard Deviation:")
print(std_deviation_values)

print("\nVariance:")
print(variance_values)

plt.figure(figsize=(12, 8))
sns.scatterplot(x='Longitude', y='Latitude', data=df, hue='Area Code', palette='viridis', s=50)
plt.title('Spatial Distribution of Cell Towers')
plt.show()
