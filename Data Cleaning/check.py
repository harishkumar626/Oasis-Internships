import pandas as pd

# Load the dataset
file_path = "C:\\Users\\WELCOME\\Desktop\\intern\\Cleaning Data\\AB_NYC_2019.csv"
df = pd.read_csv(file_path)

# Display the first few rows of the dataset
df.head()

missing_values = df.isnull().sum()
missing_values

df['name'].fillna('Unknown', inplace=True)
df['host_name'].fillna('Unknown', inplace=True)
df['reviews_per_month'].fillna(0, inplace=True)

# Check for duplicate rows
duplicate_rows = df.duplicated().sum()
duplicate_rows

df['name'] = df['name'].str.strip().str.title()
df['host_name'] = df['host_name'].str.strip().str.title()
df['neighbourhood_group'] = df['neighbourhood_group'].str.strip().str.title()
df['neighbourhood'] = df['neighbourhood'].str.strip().str.title()
df['room_type'] = df['room_type'].str.strip().str.title()

# Convert data types
df['last_review'] = pd.to_datetime(df['last_review'], errors='coerce')

# Display the updated dataframe info to check data types
df.info()
