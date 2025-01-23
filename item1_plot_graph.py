import matplotlib.pyplot as plt
import numpy as np


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

    fig, axs = plt.subplots(2, 2, figsize=(10, 8))

    axs[0, 0].plot(x, y1, 'r-', label="x^2")
    axs[0, 0].set_title("f(x) = x^2")
    axs[0, 0].set_xlabel("x")
    axs[0, 0].set_ylabel("y = x^2")
    axs[0, 0].legend()

    axs[0, 1].plot(x, y2, 'g-', label="x*sin(2*x)")
    axs[0, 1].set_title("f(x) = x * sin(2*x)")
    axs[0, 1].set_xlabel("x")
    axs[0, 1].set_ylabel("y = arctan(x)")
    axs[0, 1].legend()


    axs[1, 0].plot(x, y3, 'c-', label="arctan(x)")
    axs[1, 0].set_title("f(x) = arctg(x)")
    axs[1, 0].set_xlabel("x")
    axs[1, 0].set_ylabel("y = arctan(x)")
    axs[1, 0].legend()


    axs[1, 1].axis('off')

    plt.tight_layout()

    plt.show()