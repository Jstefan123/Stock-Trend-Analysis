from database import *
from plot import createLineGraph

def main():

    data = getDOWStock('AAPL')
    createLineGraph(data)

if __name__ == "__main__":
    main()
