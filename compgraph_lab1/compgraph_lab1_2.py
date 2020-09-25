from tkinter import *
import math
from graphics import *
root = Tk()


def task1_def():
    global window1
    if window1 == None:
        window1 = GraphWin("Вікно для графіки", 500, 500)
        a = 150
        b = 350
        colors = ["red", "orange", "lime", "purple"]
        f = 0
        for i in (-5, 20, 40, 75):
            obj1 = Line(Point(a + i, a + i), Point(a + i, b - i))
            obj2 = Line(Point(a + i, a + i), Point(b - i, a + i))
            obj3 = Line(Point(b - i, b - i), Point(a + i, b - i))
            obj4 = Line(Point(b - i, b - i), Point(b - i, a + i))

            obj1.setOutline(colors[f])
            obj2.setOutline(colors[f])
            obj3.setOutline(colors[f])
            obj4.setOutline(colors[f])

            obj1.setWidth(3)
            obj2.setWidth(3)
            obj3.setWidth(3)
            obj4.setWidth(3)

            obj1.draw(window1)
            obj2.draw(window1)
            obj3.draw(window1)
            obj4.draw(window1)
            f += 1

        obj1 = Line(Point(210, 220), Point(210, 280))
        obj2 = Line(Point(210, 220), Point(290, 220))
        obj3 = Line(Point(290, 280), Point(210, 280))
        obj4 = Line(Point(290, 280), Point(290, 220))

        obj1.setWidth(3)
        obj2.setWidth(3)
        obj3.setWidth(3)
        obj4.setWidth(3)

        obj1.setOutline("skyblue")
        obj2.setOutline("skyblue")
        obj3.setOutline("skyblue")
        obj4.setOutline("skyblue")

        obj1.draw(window1)
        obj2.draw(window1)
        obj3.draw(window1)
        obj4.draw(window1)


    else:
        window1.destroy()
        window1 = None


def task2_1_def():
    global window2_1
    if window2_1 == None:
        window2_1 = GraphWin("Вікно для графіки", 550, 400)
        obj1 = Polygon(Point(350, 50), Point(450, 150), Point(350, 250), Point(250, 150))
        obj2 = Polygon(Point(275, 100), Point(375, 200), Point(275, 300), Point(175, 200))
        obj3 = Polygon(Point(350, 150), Point(450, 250), Point(350, 350), Point(250, 250))
        obj4 = Polygon(Point(425, 100), Point(525, 200), Point(425, 300), Point(325, 200))

        obj1.setWidth(3)
        obj2.setWidth(3)
        obj3.setWidth(3)
        obj4.setWidth(3)

        obj1.setFill("skyblue")
        obj2.setFill("skyblue")
        obj3.setFill("skyblue")
        obj4.setFill("skyblue")

        obj1.setOutline("skyblue")
        obj2.setOutline("skyblue")
        obj3.setOutline("skyblue")
        obj4.setOutline("skyblue")

        obj1.draw(window2_1)
        obj2.draw(window2_1)
        obj3.draw(window2_1)
        obj4.draw(window2_1)




    else:
        window2_1.destroy()
        window2_1 = None


def task2_2_def():
    global window2_2
    if window2_2 == None:
        window2_2 = GraphWin("Вікно для графіки", 550, 400)
        obj1 = Polygon(Point(350, 50), Point(450, 150), Point(350, 250), Point(250, 150))
        obj2 = Polygon(Point(275, 100), Point(375, 200), Point(275, 300), Point(175, 200))
        obj3 = Polygon(Point(350, 150), Point(450, 250), Point(350, 350), Point(250, 250))
        obj4 = Polygon(Point(425, 100), Point(525, 200), Point(425, 300), Point(325, 200))

        obj1.setWidth(3)
        obj2.setWidth(3)
        obj3.setWidth(3)
        obj4.setWidth(3)

        obj1.setFill("red")
        obj2.setFill("orange")
        obj3.setFill("skyblue")
        obj4.setFill("lime")

        obj1.setOutline("darkred")
        obj2.setOutline("darkorange")
        obj3.setOutline("blue")
        obj4.setOutline("green")

        obj1.draw(window2_2)
        obj2.draw(window2_2)
        obj3.draw(window2_2)
        obj4.draw(window2_2)




    else:
        window2_2.destroy()
        window2_2 = None


def task3_1_def():
    global window3
    if window3 == None:
        window3 = GraphWin("Вікно для графіки", 700, 200)
        e = Canvas(window3, width=700, height=200, bg='white')
        a = 26
        points1 = []
        for x in range(500):
            y = 3 * 0.01 * 26 * math.sin(-x)
            points1.append(tuple([x * 50 + 100, y * 50 + 100]))
        e.create_line(points1, fill="red", smooth=1, width=3)

        a = 26
        points2 = []
        for x in range(500):
            y = 3 * 0.01 * 26 * math.cos(-x)
            points2.append(tuple([x * 50 + 100, y * 50 + 100]))
        e.create_line(points2, fill="lime", smooth=1, width=3)

    else:
        window3.destroy()
        window3 = None


task1_button = Button(root, text="Завдання 1", command=task1_def)
task2_1_button = Button(root, text="Завдання 2.1", command=task2_1_def)
task2_2_button = Button(root, text="Завдання 2.2", command=task2_2_def)
task3_1_button = Button(root, text="Завдання 3.1", command=task3_1_def)

window1 = None
window2_1 = None
window2_2 = None
window3 = None

task1_button.pack()
task2_1_button.pack()
task2_2_button.pack()
task3_1_button.pack()
root.mainloop()