from database import *
from plot import singleStockLineGraph

def main():

    data = getDOWStock('AAPL')
    print(data)
    singleStockLineGraph(data)

if __name__ == "__main__":
    main()
