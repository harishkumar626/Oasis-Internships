import pandas as pd

# Load the dataset
file_path = "C:\\Users\\WELCOME\\Desktop\\intern\\Exploratory Data Analysis (EDA) on Retail Sales Data\\retail_sales_dataset.csv"
retail_sales_df = pd.read_csv(file_path)

# Display basic information about the dataset
retail_sales_df.info(), retail_sales_df.head()

# Descriptive statistics of the dataset
descriptive_stats = retail_sales_df.describe(include='all')
descriptive_stats

import matplotlib.pyplot as plt

# Convert 'Date' column to datetime format
retail_sales_df['Date'] = pd.to_datetime(retail_sales_df['Date'])

# Group by date and sum the total amounts
sales_over_time = retail_sales_df.groupby('Date')['Total Amount'].sum()

# Plot sales over time
plt.figure(figsize=(14, 7))
plt.plot(sales_over_time.index, sales_over_time.values, marker='o', linestyle='-', color='b')
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Group by product category and sum the total amounts
sales_by_category = retail_sales_df.groupby('Product Category')['Total Amount'].sum()

# Plot sales by product category
plt.figure(figsize=(10, 6))
sales_by_category.plot(kind='bar', color=['skyblue', 'orange', 'green'])
plt.title('Total Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
