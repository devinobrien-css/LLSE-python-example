import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from numpy.polynomial import polynomial as P

def main():
    X=[]
    x=[]
    y=[]

    # import dataset
    with open('hw2.dat') as file:
        for row in file:
            data_in = row.split(' ')
            X.append([float(data_in[0]),float(data_in[1])])
            x.append(float(data_in[0]))
            y.append(float(data_in[1]))

    fig, axs = plt.subplots(2,2)

    # degree 1
    coef,resid,rank,sing,cond = np.polyfit(x, y, 1, full=True)
    print(f'''DEGREE 1:
-------------------------------------------
coefficients/parameters: {coef}
residual/optimal error: {resid}
''')
    axs[0,0].plot(x, y, '.', color="red")
    axs[0,0].plot(x, np.polyval(coef, x))
    axs[0,0].set_title('Polynomial order 1')

    # degree 3
    coef,resid,rank,sing,cond = np.polyfit(x, y, 3, full=True)
    print(f'''DEGREE 3:
-------------------------------------------
coefficients/parameters: {coef}
residual/optimal error: {resid}
''')
    axs[0,1].plot(x, y, '.', color="red")
    axs[0,1].plot(x, np.polyval(coef, x))
    axs[0,1].set_title('Polynomial order 3')

    # degree 5
    coef,resid,rank,sing,cond = np.polyfit(x, y, 5, full=True)
    print(f'''DEGREE 5:
-------------------------------------------
coefficients/parameters: {coef}
residual/optimal error: {resid}
''')
    axs[1,0].plot(x, y, '.', color="red")
    axs[1,0].plot(x, np.polyval(coef, x))
    axs[1,0].set_title('Polynomial order 5')

    # degree 7
    coef,resid,rank,sing,cond = np.polyfit(x, y, 7, full=True)
    print(f'''DEGREE 7:
-------------------------------------------
coefficients/parameters: {coef}
residual/optimal error: {resid}
''')
    axs[1,1].plot(x, y, '.', color="red")
    axs[1,1].plot(x, np.polyval(coef, x))
    axs[1,1].set_title('Polynomial order 7')

    plt.show()

if __name__ == '__main__':
    main()