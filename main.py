import pandas as p
import matplotlib.pyplot as plt

# Enzo : Owners
# Mathis : Sales
# Me : Transactions (txns)


def show_graph(data: p.DataFrame, name: str):
    """
    This function shows a bar chart with y datas of the 10 first NFT collection.
    @param: data, x, y
    @return: matplotlib chart
    """
    ordered_data = data.sort_values(name)
    y = ordered_data[name].head(10)
    x = ordered_data['Collections'].head(10)
    plt.title(name)
    plt.bar(x, y)
    plt.show()


def main():
    data = p.read_csv('nft_sales.csv')
    # Show transactions
    show_graph(data, 'Txns')
    # Show Sales
    show_graph(data, 'Sales')
    # Show Owners
    show_graph(data, 'Owners')


if __name__ == "__main__":
    main()
