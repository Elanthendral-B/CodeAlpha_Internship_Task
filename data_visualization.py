import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("dataset/online_retail.csv")

# Data Cleaning
df = df.drop_duplicates()
df["Description"] = df["Description"].fillna("Unknown")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Remove invalid values
df = df[df["Quantity"] > 0]
df = df[df["UnitPrice"] > 0]

# Calculate Total Sales
df["TotalSales"] = df["Quantity"] * df["UnitPrice"]

print("Dataset loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))
# Monthly Sales Trend

df["Month"] = df["InvoiceDate"].dt.to_period("M")

monthly_sales = df.groupby("Month")["TotalSales"].sum()

plt.figure(figsize=(12, 6))
plt.plot(monthly_sales.index.astype(str), monthly_sales.values, marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
# Top 10 Best-Selling Products

top_products = (
    df.groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))
sns.barplot(
    x=top_products.values,
    y=top_products.index
)

plt.title("Top 10 Best-Selling Products")
plt.xlabel("Quantity Sold")
plt.ylabel("Product")
plt.tight_layout()

plt.show()
# Top 10 Countries by Sales
country_sales = df.groupby("Country")["TotalSales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(
    x=country_sales.values,
    y=country_sales.index
)

plt.title("Top 10 Countries by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Country")
plt.tight_layout()

plt.show()
plt.savefig("output/monthly_sales_trend.png")
plt.show()
plt.savefig("output/top_10_products.png")
plt.show()