import pandas as pd

# ==========================================
# CODEALPHA INTERNSHIP - TASK 2
# Exploratory Data Analysis (EDA)
# ==========================================

# 1. Load Dataset
df = pd.read_csv("dataset/online_retail.csv")

print("=" * 50)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 50)

# 2. Display First 5 Rows
print("\n1. First 5 Rows:")
print(df.head())

# 3. Dataset Information
print("\n2. Dataset Information:")
print(df.info())

# 4. Dataset Shape
print("\n3. Dataset Shape:")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 5. Missing Values
print("\n4. Missing Values:")
print(df.isnull().sum())

# 6. Duplicate Rows
print("\n5. Duplicate Rows:")
print(df.duplicated().sum())

# ==========================================
# DATA CLEANING
# ==========================================

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing descriptions
df["Description"] = df["Description"].fillna("Unknown")

# Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Remove invalid quantity values
df = df[df["Quantity"] > 0]

# Remove invalid unit prices
df = df[df["UnitPrice"] > 0]

print("\n6. After Data Cleaning:")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# ==========================================
# SALES ANALYSIS
# ==========================================

# Calculate Total Sales
df["TotalSales"] = df["Quantity"] * df["UnitPrice"]

# Sales Statistics
print("\n7. Sales Statistics:")
print(df["TotalSales"].describe())

# Total Revenue
print("\n8. Total Revenue:")
print(round(df["TotalSales"].sum(), 2))

# ==========================================
# TOP 10 BEST-SELLING PRODUCTS
# ==========================================

top_products = (
    df.groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n9. Top 10 Best-Selling Products:")
print(top_products)

# ==========================================
# COUNTRY-WISE SALES
# ==========================================

country_sales = (
    df.groupby("Country")["TotalSales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n10. Top 10 Countries by Sales:")
print(country_sales)

# ==========================================
# MONTHLY SALES ANALYSIS
# ==========================================

df["Month"] = df["InvoiceDate"].dt.to_period("M")

monthly_sales = df.groupby("Month")["TotalSales"].sum()

print("\n11. Monthly Sales:")
print(monthly_sales)

# ==========================================
# END
# ==========================================

print("\n" + "=" * 50)
print("EDA ANALYSIS COMPLETED SUCCESSFULLY!")
print("=" * 50)