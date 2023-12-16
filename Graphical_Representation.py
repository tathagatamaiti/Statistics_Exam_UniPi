import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = r"C:\Users\Tathagata\Downloads\208.csv"
df = pd.read_csv(file_path)

plt.figure(figsize=(16, 8))

plt.subplot(2, 2, 1)
sns.histplot(df['Longitude'], bins=20, kde=True, color='skyblue')
plt.title('Histogram of Longitude')

plt.subplot(2, 2, 2)
sns.histplot(df['Latitude'], bins=20, kde=True, color='salmon')
plt.title('Histogram of Latitude')

plt.subplot(2, 2, 3)
sns.histplot(df['Range'], bins=20, kde=True, color='green')
plt.title('Histogram of Range in meters')

plt.subplot(2, 2, 4)
sns.histplot(df['Number of Samples'], bins=20, kde=True, color='orange')
plt.title('Histogram of Number of Samples')

plt.tight_layout()
plt.show()

plt.figure(figsize=(16, 8))

plt.subplot(2, 2, 1)
sns.boxplot(x=df['Longitude'], color='skyblue')
plt.title('Box Plot of Longitude')

plt.subplot(2, 2, 2)
sns.boxplot(x=df['Latitude'], color='salmon')
plt.title('Box Plot of Latitude')

plt.subplot(2, 2, 3)
sns.boxplot(x=df['Range'], color='green')
plt.title('Box Plot of Range in meters')

plt.subplot(2, 2, 4)
sns.boxplot(x=df['Number of Samples'], color='orange')
plt.title('Box Plot of Number of Samples')

plt.tight_layout()
plt.show()

plt.figure(figsize=(16, 8))

plt.subplot(2, 2, 1)
sns.scatterplot(x='Longitude', y='Range', data=df, color='skyblue')
plt.title('Scatter Plot: Longitude vs. Range in meters')

plt.subplot(2, 2, 2)
sns.scatterplot(x='Longitude', y='Number of Samples', data=df, color='salmon')
plt.title('Scatter Plot: Longitude vs. Number of Samples')

plt.subplot(2, 2, 3)
sns.scatterplot(x='Latitude', y='Range', data=df, color='green')
plt.title('Scatter Plot: Latitude vs. Range in meters')

plt.subplot(2, 2, 4)
sns.scatterplot(x='Latitude', y='Number of Samples', data=df, color='orange')
plt.title('Scatter Plot: Latitude vs. Number of Samples')

plt.tight_layout()
plt.show()
