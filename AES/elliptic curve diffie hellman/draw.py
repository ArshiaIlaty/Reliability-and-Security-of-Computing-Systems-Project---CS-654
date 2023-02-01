import numpy as np
import matplotlib.pyplot as plt
import math
def main():
    
    fig = plt.figure()
    ax = fig.add_subplot(111)

    y, x = np.ogrid[-2:2:1000j, -2:2:1000j]
    ax.contour(x.ravel(), y.ravel(), pow(y, 2) + pow(-x, 3) + pow(-x, 1) , [6],colors='red')
    ax.plot(0, 0, color="red", marker = "o", markersize = 2.5, zorder = 10)

    ax.grid()
    plt.show()

if __name__ == '__main__':
    main()

