import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



def main():
    x=[]
    y=[]
    with open('hw2.dat') as file:
        for row in file:
            data_in = row.split(' ')
            x.append(float(data_in[0]))
            y.append(float(data_in[1]))
    
    plt.title('Degree 1')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.scatter(x,y)
    plt.show()

if __name__ == '__main__':
    main()