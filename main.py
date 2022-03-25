import pandas as p
import matplotlib.pyplot as plt

# Enzo : Owners
# Mathis : Sales
# Me : Transactions (txns)

def txns_graph(data: p.DataFrame):
    """
    This function print a chart with the 10 Collections with the most transactions 
    in the dataset, with their height the Txns column associated values.
    @param: p.DataFrame
    """
    y = data['Txns'].head(10)
    x = data['Collections'].head(10)
    plt.bar(x, y)
    plt.show()
    
def main():
    data = p.read_csv('nft_sales.csv')
    txns_graph(data)
    

if __name__ == "__main__":
    main()
