def analyze_data(df):
    df["Total_Sales"] = df["Quantity"] * df["Price"]

    total_sales = df["Total_Sales"].sum()
    category_sales = df.groupby("Category")["Total_Sales"].sum()

    return total_sales, category_sales