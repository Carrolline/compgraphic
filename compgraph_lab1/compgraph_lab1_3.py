import matplotlib.pyplot as plt
from tkinter import *
import math
import numpy as np
root = Tk()


def task1_def():
    plt.plot([0, 0, 100, 100, 0], [0, 100, 100, 0, 0], color="red", linewidth=3)
    plt.plot([10, 10, 90, 90, 10], [10, 90, 90, 10, 10], color="orange", linewidth=3)
    plt.plot([20, 20, 80, 80, 20], [20, 80, 80, 20, 20], color="lime", linewidth=3)
    plt.plot([30, 30, 70, 70, 30], [35, 65, 65, 35, 35], color="skyblue", linewidth=3)
    plt.plot([40, 40, 60, 60, 40], [40, 60, 60, 40, 40], color="purple", linewidth=3)
    plt.show()


def task2_1_def():
    x1 = [40, 60, 40, 20, 40]
    y1 = [60, 40, 20, 40, 60]
    x2 = [55, 75, 55, 35, 55]
    y2 =[50, 30, 10, 30, 50]
    x3 = [40, 60, 40, 20, 40]
    y3 = [40, 20, 0, 20, 40]
    x4 = [25, 45, 25, 5, 25]
    y4 = [50, 30, 10, 30, 50]

    plt.fill(x1, y1, linewidth=3, edgecolor="darkred", facecolor="red")
    plt.fill(x2, y2, linewidth=3, edgecolor="darkorange", facecolor="orange")
    plt.fill(x3, y3, linewidth=3, edgecolor="blue", facecolor="deepskyblue")
    plt.fill(x4, y4, linewidth=3, edgecolor="green", facecolor="lime")


    plt.show()


def task2_2_def():
    x1 = [40, 60, 40, 20, 40]
    y1 = [60, 40, 20, 40, 60]
    x2 = [55, 75, 55, 35, 55]
    y2 = [50, 30, 10, 30, 50]
    x3 = [40, 60, 40, 20, 40]
    y3 = [40, 20, 0, 20, 40]
    x4 = [25, 45, 25, 5, 25]
    y4 = [50, 30, 10, 30, 50]
    fig, ax = plt.subplots()

    ax.fill(x1, y1, "skyblue")
    ax.fill(x2, y2, "skyblue")
    ax.fill(x3, y3, "skyblue")
    ax.fill(x4, y4, "skyblue")

    fig.set_figwidth(6)  # ширина и
    fig.set_figheight(5)  # высота "Figure"
    fig.set_facecolor('floralwhite')
    ax.set_facecolor('seashell')

    plt.show()
    plt.show()


def task3_1_def():
    # Независимая (x) и зависимая (y) переменные
    plt.xlabel("x", fontsize=14)  # ось абсцисс
    plt.ylabel("y", fontsize=14)  # ось ординат
    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    y = np.sin(x)

    plt.plot(x, y, color="green")
    plt.show()


def task3_2_def():
    # Независимая (x) и зависимая (y) переменные

    plt.xlabel("x", fontsize=14)  # ось абсцисс
    plt.ylabel("y", fontsize=14)  # ось ординат

    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    y = np.cos(x)

    plt.plot(x, y)
    plt.show()


def task3_3_def():
    # Choose evenly spaced x intervals
    x = np.linspace(-2*np.pi, 2*np.pi, 666)
    y = np.tan(x)
    y[np.abs(np.cos(x)) <= np.abs(np.sin(x[1]-x[0]))] = np.nan
    plt.plot(x, y, color="magenta")
    plt.ylim(-3, 3)
    plt.show()


def task3_4_def():
    # Choose evenly spaced x intervals
    x3 = np.linspace(-2*np.pi, 2*np.pi, 666)
    y3 = np.tan(x3)
    y3[np.abs(np.cos(x3)) <= np.abs(np.sin(x3[1]-x3[0]))] = np.nan
    plt.plot(x3, y3, color="magenta")
    plt.ylim(-3, 3)

    # Независимая (x) и зависимая (y) переменные

    plt.xlabel("x", fontsize=14)  # ось абсцисс
    plt.ylabel("y", fontsize=14)  # ось ординат

    x1 = np.linspace(-2 * np.pi, 2 * np.pi, 100)
    y1 = np.cos(x1)

    plt.plot(x1, y1)

    x2 = np.linspace(-2 * np.pi, 2 * np.pi, 100)
    y2 = np.sin(x2)

    plt.plot(x2, y2, color="green")

    plt.show()



task1_button = Button(root, text="Завдання 1", command=task1_def)
task2_1_button = Button(root, text="Завдання 2.1", command=task2_1_def)
task2_2_button = Button(root, text="Завдання 2.2", command=task2_2_def)
task3_1_button = Button(root, text="Завдання 3.1", command=task3_1_def)
task3_2_button = Button(root, text="Завдання 3.2", command=task3_2_def)
task3_3_button = Button(root, text="Завдання 3.3", command=task3_3_def)
task3_4_button = Button(root, text="Завдання 3.4", command=task3_4_def)



task1_button.pack()
task2_1_button.pack()
task2_2_button.pack()
task3_1_button.pack()
task3_2_button.pack()
task3_3_button.pack()
task3_4_button.pack()
root.mainloop()