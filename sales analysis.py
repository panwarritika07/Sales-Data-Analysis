import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv ("Sales_Data_Analyst_project.csv")
print(df.head())
# print(df.shape)
# print(df.columns)
# print(df.info())
df = df.drop(columns=["Unnamed: 11", "Unnamed: 12", "Unnamed: 13"])
# print(df.shape)
# print(df.columns)
# Check duplicate Order IDs
# Remove completely empty rows
df = df.dropna(how="all")

# Check dataset shape
print("Dataset shape:", df.shape)

# Check duplicate Order IDs
print("Duplicate Order IDs:",
      df["Order_ID"].duplicated().sum())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())
print("\nFinal columns:")
print(df.columns)
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
print(df.info())
df["Year"] = df["Order_Date"].dt.year
df["Month"] = df["Order_Date"].dt.month
df["Month_Name"] = df["Order_Date"].dt.month_name()
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
print(df.info())
print("\nBasic Statistics:")
print(df.describe())
# # Business KPIs

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
total_orders = df["Order_ID"].nunique()

print("\nBusiness KPIs")
print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Total Quantity Sold:", total_quantity)
print("Total Orders:", total_orders)
# Additional KPIs

profit_margin = (total_profit / total_sales) * 100
average_order_value = total_sales / total_orders

print("Profit Margin:", round(profit_margin, 2), "%")
print("Average Order Value:", round(average_order_value, 2))
# Additional KPIs

# Sales and Profit by Category

category_analysis = df.groupby("Category")[["Sales", "Profit"]].sum()

category_analysis = category_analysis.sort_values(
    by="Sales",
    ascending=False
)

print("\nSales and Profit by Category:")
print(category_analysis)
# Sales and Profit by Region

region_analysis = df.groupby("Region")[["Sales", "Profit"]].sum()

region_analysis = region_analysis.sort_values(
    by="Sales",
    ascending=False
)

print("\nSales and Profit by Region:")
print(region_analysis)
# Top 10 Products by Sales

top_products = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products by Sales:")
print(top_products)
# Top 10 Customers by Sales

top_customers = (
    df.groupby("Customer")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Customers by Sales:")
print(top_customers)
# Top 10 Customers by Sales

top_customers = (
    df.groupby("Customer")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Customers by Sales:")
print(top_customers)
# Monthly Sales Analysis

monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
    .sort_index()
)

print("\nMonthly Sales:")
print(monthly_sales)
# Monthly Sales Chart

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(range(1, 13))

plt.tight_layout()
plt.show()
# # Sales by Category Chart

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8, 5))

plt.bar(category_sales.index, category_sales.values)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()
# Sales by Region Chart

region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8, 5))

plt.bar(region_sales.index, region_sales.values)

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()
# Top 10 Products Sales Chart

top_products = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))

plt.barh(top_products.index[::-1], top_products.values[::-1])

plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")
plt.ylabel("Product")

plt.tight_layout()
plt.show()
# Save cleaned dataset

df.to_csv("cleaned_sales_data.csv", index=False)

print("Cleaned dataset saved successfully.")
