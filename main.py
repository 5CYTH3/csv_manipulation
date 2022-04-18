from matplotlib.container import BarContainer
import pandas as p
import matplotlib.pyplot as plt

# Enzo : Owners
# Mathis : Sales
# Me : Transactions (txns)


def show_bar_chart(data: p.DataFrame, name: str, color: str, fig_id: int) -> BarContainer:
    """
    This function shows a bar chart with y datas of the 10 first NFT collection.
    @param: data<DataFrame>, name<str>, color<str>, fig_id<int>
    @return: BarContainer
    """
    ordered_data = data.sort_values(name)
    y = ordered_data[name].head(10)
    x = ordered_data['Collections'].head(10)
    plt.title(name)
    f = plt.figure(fig_id)
    return plt.bar(x=x, height=y, color=color)
    


def show_pie_chart(data: p.DataFrame, name: str, fig_id: int) -> any:
    """
    This function shows a pie chart with data of the first 5 NFT collections.
    @param: data<DataFrame>, name<str>
    @return: matplotlib pie chart <any>
    """
    ordered_data = data.sort_values(name)
    plt.title(name)
    labels = ordered_data['Collections'].head(5)
    values = ordered_data[name].head(5)
    f = plt.figure(fig_id)
    try:
        return plt.pie(values, labels=labels)
    except ValueError:
        values = values.replace('[\$,]', '', regex=True).astype(float)
        return plt.pie(values, labels=labels, autopct='%4.f %%')


def main():
    data = p.read_csv('nft_sales.csv')
    # Show transactions
    show_bar_chart(data, 'Txns', 'blue', 1)
    # Show Sales
    show_pie_chart(data, 'Sales', 2)
    # Show Owners
    show_bar_chart(data, 'Owners', 'green', 3)
    plt.show()



if __name__ == "__main__":
    main()
