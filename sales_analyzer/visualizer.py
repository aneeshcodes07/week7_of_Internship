import matplotlib.pyplot as plt

def plot_category_sales(category_sales):
    category_sales.plot(kind="bar")
    plt.title("Sales by Category")
    plt.ylabel("Total Sales")
    plt.show()