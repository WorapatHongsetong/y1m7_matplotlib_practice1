import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt

def square(start, stop, size):
    x = np.linspace(start=start, stop=stop, num=size)
    y = x ** 2
    return x, y

def xsin_2x(start, stop, size):
    x = np.linspace(start=start, stop=stop, num=size)
    y = x * np.sin(2 * x)
    return x, y

def arctg(start, stop, size):
    x = np.linspace(start=start, stop=stop, num=size)
    y = np.arctan(x)
    return x, y




if __name__ == "__main__":
    START, STOP, SIZE = -10, 10, 200

    x, y1 = square(START, STOP, SIZE)
    y2 = xsin_2x(START, STOP, SIZE)[1]
    y3 = arctg(START, STOP, SIZE)[1]

    # fig, axs = plt.subplots(2, 2, figsize=(10, 8))

    # axs[0, 0].plot(x, y1, color='#f00', linestyle="solid", label="x^2", marker="o", markersize=2)
    # axs[0, 0].set_title("f(x) = x^2")
    # axs[0, 0].set_xlabel("x")
    # axs[0, 0].set_ylabel("y = x^2")
    # axs[0, 0].legend()

    # axs[0, 1].plot(x, y2, color='#0f0', linestyle="dotted", label="x*sin(2*x)", marker="o", markersize=2)
    # axs[0, 1].set_title("f(x) = x * sin(2*x)")
    # axs[0, 1].set_xlabel("x")
    # axs[0, 1].set_ylabel("y = arctan(x)")
    # axs[0, 1].legend()


    # axs[1, 0].plot(x, y3, color='#6d6d6d', linestyle="dashed", label="arctan(x)", marker="o", markersize=2)
    # axs[1, 0].set_title("f(x) = arctg(x)")
    # axs[1, 0].set_xlabel("x")
    # axs[1, 0].set_ylabel("y = arctan(x)")
    # axs[1, 0].legend()


    # axs[1, 1].axis('off')

    # plt.tight_layout()

    # plt.show()


    plt.plot(x, y1, color='#f00', linestyle="solid", label="x^2", marker="o", markersize=2)
    plt.plot(x, y2, color='#0f0', linestyle="dotted", label="x*sin(2*x)", marker="o", markersize=2)
    plt.plot(x, y3, color='#6d6d6d', linestyle="dashed", label="arctan(x)", marker="o", markersize=2)
    plt.title("Multiple function")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.ylim((-10, 10))

    plt.show()