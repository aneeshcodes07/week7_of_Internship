from sales_analyzer.data_loader import load_data
from sales_analyzer.data_cleaner import clean_data
from sales_analyzer.analyzer import analyze_data
from sales_analyzer.visualizer import plot_category_sales
from sales_analyzer.reporter import generate_report

def main():
    file_path = "data/sales_data.csv"

    df = load_data(file_path)
    df = clean_data(df)

    total_sales, category_sales = analyze_data(df)

    generate_report(total_sales)
    plot_category_sales(category_sales)

if __name__ == "__main__":
    main()