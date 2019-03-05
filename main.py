from database import *
from plot import *

def main():

    data = getDOWStock('AAPL')
    
    singleStockLineGraph(data)

if __name__ == "__main__":
    main()
