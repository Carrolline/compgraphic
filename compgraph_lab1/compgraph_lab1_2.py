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
    global window3_1
    if window3_1 == None:
        window3_1 = GraphWin("Вікно для графіки", 700, 200)
        Text(Point(680, 90), "X").draw(window3_1)
        Text(Point(425, 20), "Y").draw(window3_1)
        Line(Point(100, 100), Point(697, 100)).draw(window3_1)
        Line(Point(415, 200), Point(415, 3)).draw(window3_1)
        # arrow right
        Line(Point(697, 100), Point(687, 90)).draw(window3_1)
        Line(Point(697, 100), Point(687, 110)).draw(window3_1)
        # arrow top
        Line(Point(415, 3), Point(425, 13)).draw(window3_1)
        Line(Point(415, 3), Point(405, 13)).draw(window3_1)
        a = 26
        f1 = 0
        points1 = []
        points1_1 = []
        while f1 < 10 * math.pi / 2:
            points1.append(f1)
            f1 += 0.1

        for x in points1:
            y = 3 * 0.01 * 26 * math.sin(-x)
            points1_1.append(tuple([x * 50 + 100, y * 50 + 100]))
        for i in range(1, len(points1_1)):
            obj = Line(Point(points1_1[i - 1][0], points1_1[i - 1][1]), Point(points1_1[i][0], points1_1[i][1]))
            obj.setOutline("deepskyblue")
            obj.setWidth(2)
            obj.draw(window3_1)


    else:
        window3_1.destroy()
        window3_1 = None


def task3_2_def():
    global window3_2
    if window3_2 == None:
        window3_2 = GraphWin("Вікно для графіки", 700, 200)
        Text(Point(680, 90), "X").draw(window3_2)
        Text(Point(425, 20), "Y").draw(window3_2)
        Line(Point(100, 100), Point(697, 100)).draw(window3_2)
        Line(Point(415, 200), Point(415, 3)).draw(window3_2)
        # arrow right
        Line(Point(697, 100), Point(687, 90)).draw(window3_2)
        Line(Point(697, 100), Point(687, 110)).draw(window3_2)
        # arrow top
        Line(Point(415, 3), Point(425, 13)).draw(window3_2)
        Line(Point(415, 3), Point(405, 13)).draw(window3_2)

        a = 26
        f2 = 0
        points2 = []
        points2_1 = []
        while f2 < 10*math.pi / 2:
            points2.append(f2)
            f2 += 0.1

        for x in points2:
            y = 3 * 0.01 * 26 * math.cos(x)
            points2_1.append(tuple([x * 50 + 100, -y * 50 + 100]))
        for i in range(1, len(points2_1)):
            obj = Line(Point(points2_1[i-1][0], points2_1[i-1][1]), Point(points2_1[i][0], points2_1[i][1]))
            obj.setOutline("lime")
            obj.setWidth(2)
            obj.draw(window3_2)
        print(points2_1)
    else:
        window3_2.destroy()
        window3_2 = None


def task3_3_def():
    global window3_3
    if window3_3 == None:
        window3_3 = GraphWin("Вікно для графіки", 700, 200)
        Text(Point(680, 90), "X").draw(window3_3)
        Text(Point(425, 20), "Y").draw(window3_3)
        Line(Point(100, 100), Point(697, 100)).draw(window3_3)
        Line(Point(415, 200), Point(415, 3)).draw(window3_3)
        # arrow right
        Line(Point(697, 100), Point(687, 90)).draw(window3_3)
        Line(Point(697, 100), Point(687, 110)).draw(window3_3)
        # arrow top
        Line(Point(415, 3), Point(425, 13)).draw(window3_3)
        Line(Point(415, 3), Point(405, 13)).draw(window3_3)
        a = 26
        points2 = []
        ################################
        a = 26
        points3_1 = []
        points3_2 = []
        points3_3 = []
        points3_4 = []
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        f1 = 0
        while f1 < math.pi / 2:
            list1.append(f1)
            f1 += 0.1
        for x in list1:
            y = 3 * 0.01 * 26 * math.tan(-x)
            points3_1.append(tuple([x * 50 + 100, y * 50 + 100]))
        for i in range(1, len(points3_1)):
            obj = Line(Point(points3_1[i - 1][0], points3_1[i - 1][1]), Point(points3_1[i][0], points3_1[i][1]))
            obj.setOutline("red")
            obj.setWidth(2)
            obj.draw(window3_3)

        f2 = math.pi / 2 + 0.1
        while f2 < 3 * math.pi / 2:
            list2.append(f2)
            f2 += 0.1
        for x in list2:
            y = 3 * 0.01 * 26 * math.tan(-x)
            points3_2.append(tuple([x * 50 + 100, y * 50 + 100]))
        for i in range(1, len(points3_2)):
            obj = Line(Point(points3_2[i - 1][0], points3_2[i - 1][1]), Point(points3_2[i][0], points3_2[i][1]))
            obj.setOutline("red")
            obj.setWidth(2)
            obj.draw(window3_3)

        f3 = 3 * math.pi / 2 + 0.1
        while f3 < 5 * math.pi / 2:
            list3.append(f3)
            f3 += 0.1
        for x in list3:
            y = 3 * 0.01 * 26 * math.tan(-x)
            points3_3.append(tuple([x * 50 + 100, y * 50 + 100]))
        for i in range(1, len(points3_3)):
            obj = Line(Point(points3_3[i - 1][0], points3_3[i - 1][1]), Point(points3_3[i][0], points3_3[i][1]))
            obj.setOutline("red")
            obj.setWidth(2)
            obj.draw(window3_3)

        f4 = 5 * math.pi / 2 + 0.1
        while f4 < 7 * math.pi / 2:
            list4.append(f4)
            f4 += 0.1
        for x in list4:
            y = 3 * 0.01 * 26 * math.tan(-x)
            points3_4.append(tuple([x * 50 + 100, y * 50 + 100]))
        for i in range(1, len(points3_4)):
            obj = Line(Point(points3_4[i - 1][0], points3_4[i - 1][1]), Point(points3_4[i][0], points3_4[i][1]))
            obj.setOutline("red")
            obj.setWidth(2)
            obj.draw(window3_3)

        #################################

    else:
        window3_3.destroy()
        window3_3 = None


def task3_4_def():
    global window3_4
    if window3_4 == None:
        window3_4 = GraphWin("Вікно для графіки", 700, 200)
        Text(Point(680, 90), "X").draw(window3_4)
        Text(Point(425, 20), "Y").draw(window3_4)
        Line(Point(100, 100), Point(697, 100)).draw(window3_4)
        Line(Point(415, 200), Point(415, 3)).draw(window3_4)
        # arrow right
        Line(Point(697, 100), Point(687, 90)).draw(window3_4)
        Line(Point(697, 100), Point(687, 110)).draw(window3_4)
        # arrow top
        Line(Point(415, 3), Point(425, 13)).draw(window3_4)
        Line(Point(415, 3), Point(405, 13)).draw(window3_4)
        a = 26
        f1 = 0
        points1 = []
        points1_1 = []
        while f1 < 10 * math.pi / 2:
            points1.append(f1)
            f1 += 0.1

        for x in points1:
            y = 3 * 0.01 * 26 * math.sin(-x)
            points1_1.append(tuple([x * 50 + 100, y * 50 + 100]))
        for i in range(1, len(points1_1)):
            obj = Line(Point(points1_1[i - 1][0], points1_1[i - 1][1]), Point(points1_1[i][0], points1_1[i][1]))
            obj.setOutline("deepskyblue")
            obj.setWidth(2)
            obj.draw(window3_4)

        a = 26
        f2 = 0
        points2 = []
        points2_1 = []
        while f2 < 10 * math.pi / 2:
            points2.append(f2)
            f2 += 0.1

        for x in points2:
            y = 3 * 0.01 * 26 * math.cos(x)
            points2_1.append(tuple([x * 50 + 100, -y * 50 + 100]))
        for i in range(1, len(points2_1)):
            obj = Line(Point(points2_1[i - 1][0], points2_1[i - 1][1]), Point(points2_1[i][0], points2_1[i][1]))
            obj.setOutline("lime")
            obj.setWidth(2)
            obj.draw(window3_4)
        print(points2_1)

        ######################################

        a = 26
        points3_1 = []
        points3_2 = []
        points3_3 = []
        points3_4 = []
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        f1_4 = 0
        while f1_4 < math.pi / 2:
            list1.append(f1_4)
            f1_4 += 0.1
        for x in list1:
            y = 3 * 0.01 * 26 * math.tan(-x)
            points3_1.append(tuple([x * 50 + 100, y * 50 + 100]))
        for i in range(1, len(points3_1)):
            obj = Line(Point(points3_1[i - 1][0], points3_1[i - 1][1]), Point(points3_1[i][0], points3_1[i][1]))
            obj.setOutline("red")
            obj.setWidth(2)
            obj.draw(window3_4)

        f2_4 = math.pi / 2 + 0.1
        while f2_4 < 3 * math.pi / 2:
            list2.append(f2_4)
            f2_4 += 0.1
        for x in list2:
            y = 3 * 0.01 * 26 * math.tan(-x)
            points3_2.append(tuple([x * 50 + 100, y * 50 + 100]))
        for i in range(1, len(points3_2)):
            obj = Line(Point(points3_2[i - 1][0], points3_2[i - 1][1]), Point(points3_2[i][0], points3_2[i][1]))
            obj.setOutline("red")
            obj.setWidth(2)
            obj.draw(window3_4)

        f3_3 = 3 * math.pi / 2 + 0.1
        while f3_3 < 5 * math.pi / 2:
            list3.append(f3_3)
            f3_3 += 0.1
        for x in list3:
            y = 3 * 0.01 * 26 * math.tan(-x)
            points3_3.append(tuple([x * 50 + 100, y * 50 + 100]))
        for i in range(1, len(points3_3)):
            obj = Line(Point(points3_3[i - 1][0], points3_3[i - 1][1]), Point(points3_3[i][0], points3_3[i][1]))
            obj.setOutline("red")
            obj.setWidth(2)
            obj.draw(window3_4)

        f4_4 = 5 * math.pi / 2 + 0.1
        while f4_4 < 7 * math.pi / 2:
            list4.append(f4_4)
            f4_4 += 0.1
        for x in list4:
            y = 3 * 0.01 * 26 * math.tan(-x)
            points3_4.append(tuple([x * 50 + 100, y * 50 + 100]))
        for i in range(1, len(points3_4)):
            obj = Line(Point(points3_4[i - 1][0], points3_4[i - 1][1]), Point(points3_4[i][0], points3_4[i][1]))
            obj.setOutline("red")
            obj.setWidth(2)
            obj.draw(window3_4)

    else:
        window3_4.destroy()
        window3_4 = None


task1_button = Button(root, text="Завдання 1", command=task1_def)
task2_1_button = Button(root, text="Завдання 2.1", command=task2_1_def)
task2_2_button = Button(root, text="Завдання 2.2", command=task2_2_def)
task3_1_button = Button(root, text="Завдання 3.1", command=task3_1_def)
task3_2_button = Button(root, text="Завдання 3.2", command=task3_2_def)
task3_3_button = Button(root, text="Завдання 3.3", command=task3_3_def)
task3_4_button = Button(root, text="Завдання 3.4", command=task3_4_def)

window1 = None
window2_1 = None
window2_2 = None
window3_1 = None
window3_2 = None
window3_3 = None
window3_4 = None

task1_button.pack()
task2_1_button.pack()
task2_2_button.pack()
task3_1_button.pack()
task3_2_button.pack()
task3_3_button.pack()
task3_4_button.pack()
root.mainloop()
