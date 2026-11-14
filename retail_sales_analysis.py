import pandas as pd

df =  pd.read_csv("Sample superstore.csv", encoding="latin1" )

print(df.head())
print("Dataset Shape:", df.shape)
print(df.columns.tolist())




# 1. Display first 5 rows
print("First 5 Rows:")
print(df.head())

# 2. Check dataset information
print("\nDataset Information:")
df.info()

# 3. Check number of rows and columns
print("\nDataset Shape:")
print(df.shape)

# 4. Check column names
print("\nColumn Names:")
print(df.columns.tolist())

# 5. Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# 6. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 7. Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())


# Check missing values
print("Missing Values Before Cleaning:")
print(df.isnull().sum().sum())

# Check missing values percentage
print("\nMissing Values Percentage:")
print((df.isnull().mean() * 100).round(2))

# Remove duplicate records
df = df.drop_duplicates()

print("Duplicates After Cleaning:")
print(df.duplicated().sum())

# Check rows containing missing values
missing_rows = df[df.isnull().any(axis=1)]

print("Rows with Missing Values:")
print(missing_rows.head(10))

# Convert date columns
df['Order Date'] = pd.to_datetime(df['Order Date'])

df['Ship Date'] = pd.to_datetime(df['Ship Date'])

print(df[['Order Date', 'Ship Date']].dtypes)





# Check missing values in each column
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Count rows containing missing values
print("\nTotal Rows With Missing Values:")
print(df.isnull().any(axis=1).sum())

# Check rows where Postal Code is missing
print("\nMissing Postal Code Records:")
print(df[df['Postal Code'].isnull()].head(10))

# Check total records after removing duplicates
print("\nFinal Dataset Shape:")
print(df.shape)




# Recheck missing values after duplicate removal

print("\nMissing Values Per Column:")
print(df.isnull().sum())

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

print("\nRows Containing Missing Values:")
print(df.isnull().any(axis=1).sum())

print("\nDataset Information:")
print(df.shape)


# Identify columns with missing values

missing = df.isnull().sum()

print("\nColumns With Missing Values:")

print(missing[missing > 0])

# Calculate missing value percentage

print("\nMissing Value Percentage:")

missing_percent = (df.isnull().mean() * 100).round(2)

print(missing_percent[missing_percent > 0])



# Identify rows where all columns except IDs are missing

check_columns = [
    col for col in df.columns
    if col not in ['Row ID', 'Order ID']
]

empty_records = df[
    df[check_columns].isnull().all(axis=1)
]

print("Completely Incomplete Records:")
print(empty_records.shape[0])

print("\nSample Incomplete Records:")
print(empty_records.head())


# Remove completely incomplete records

check_columns = [
    col for col in df.columns
    if col not in ['Row ID', 'Order ID']
]

df = df.dropna(subset=check_columns, how='all')

# Check dataset after cleaning
print("Dataset After Cleaning:")
print(df.shape)

print("\nRemaining Missing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

# Save cleaned dataset

df.to_csv("retail_sales_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")





import matplotlib.pyplot as plt

# Calculate total sales by category
category_sales = df.groupby('Category')['Sales'].sum()

print("\nTotal Sales by Category:")
print(category_sales)

# Create bar chart
category_sales.plot(
    kind='bar',
    figsize=(8, 5),
    title='Total Sales by Category'
)

plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("sales_category.png")
plt.show()



# Calculate sales by region

region_sales = df.groupby('Region')['Sales'].sum()

print("\nTotal Sales by Region:")
print(region_sales)

# Create bar chart

region_sales.plot(
    kind='bar',
    figsize=(8, 5),
    title='Total Sales by Region'
)

plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("sales_region.png")
plt.show()


# Calculate profit by region

region_profit = df.groupby('Region')['Profit'].sum()

print("\nTotal Profit by Region:")
print(region_profit)

# Create bar chart

region_profit.plot(
    kind='bar',
    figsize=(8, 5),
    title='Total Profit by Region'
)

plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("profit_region.png")
plt.show()
