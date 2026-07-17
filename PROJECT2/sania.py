import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\com\OneDrive\Dataset for Data Analytics (1) (1).xlsx"
df = pd.read_excel(file_path)

print(df.info())

missing_data = df.isnull().sum()
print("\n--- Missing Data Forensics ---")
print(missing_data[missing_data > 0])

summary_stats = df[['Quantity', 'UnitPrice', 'TotalPrice', 'ItemsInCart']].describe().round(2)
print("\n--- Five-Number Summary ---")
print(summary_stats)

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='OrderStatus', y='TotalPrice', palette='Set2')
plt.title('Distribution of Total Price by Order Status')
plt.xlabel('Order Status')
plt.ylabel('Total Price ($)')
sns.despine()
plt.show()

df['Month_Year'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month_Year')['TotalPrice'].sum().reset_index()
monthly_sales['Month_Year'] = monthly_sales['Month_Year'].astype(str)

plt.figure(figsize=(12, 5))
plt.plot(monthly_sales['Month_Year'], monthly_sales['TotalPrice'], marker='o', color="#4a43a0")
plt.title('Total Revenue Trend (Month-Over-Month)')
plt.xticks(rotation=45)
plt.ylabel('Total Revenue ($)')
sns.despine()
plt.show()

print("\n--- Order Status Rates ---")
print(df['OrderStatus'].value_counts(normalize=True).round(3) * 100)

product_stats = df.groupby('Product')['TotalPrice'].sum().reset_index().sort_values(by='TotalPrice', ascending=False)

plt.figure(figsize=(10, 6))
bars = sns.barplot(data=product_stats, x='Product', y='TotalPrice', color='lightgray')
bars.patches[0].set_facecolor("#AD65D2")
plt.title('Total Revenue by Product (Highlighting Top Performer)')
plt.xlabel('Product Category')
plt.ylabel('Total Revenue ($)')
sns.despine()
plt.show()
