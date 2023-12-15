import pandas as pd
print("hello")
df = pd.read_csv('music_genre.csv')
print(df.head())
print(df.info())
print(df.describe())
# df.fillna(df.mean(), inplace=True)
# df.drop_duplicates(inplace=True)
import matplotlib.pyplot as plt
plt.hist(df['popularity'], bins=20, color='blue', edgecolor='black')
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Histogram of popularity')
plt.show()