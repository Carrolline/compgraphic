from tkinter import *
import math
root = Tk()


def task1_def():
    global window1
    if window1 == None:
        window1 = Toplevel()
        c = Canvas(window1, width=500, height=500, bg='white')
        a = 150
        b = 350
        colors = ["red", "orange", "lime", "purple"]
        f = 0
        for i in (-5, 20, 40, 75):
            c.create_line(a+i, a+i, a+i, b-i, fill=colors[f], width=3)
            c.create_line(a+i, a+i, b-i, a+i, fill=colors[f], width=3)
            c.create_line(b-i, b-i, a+i, b-i, fill=colors[f], width=3)
            c.create_line(b-i, b-i, b-i, a+i, fill=colors[f], width=3)
            f += 1
        c.create_line(210, 220, 210, 280, fill="skyblue", width=3)
        c.create_line(210, 220, 290, 220, fill='skyblue', width=3)
        c.create_line(290, 280, 210, 280, fill='skyblue', width=3)
        c.create_line(290, 280, 290, 220, fill='skyblue', width=3)
        c.pack()
    else:
        window1.destroy()
        window1 = None


def task2_def():
    global window2
    if window2 == None:
        window2 = Toplevel()
        c = Canvas(window2, width=550, height=400, bg='white')
        c.create_polygon((350, 50), (450, 150), (350, 250), (250, 150),  fill="deepskyblue", outline="deepskyblue")
        c.create_polygon((275, 100), (375, 200), (275, 300), (175, 200),  fill="deepskyblue", outline="deepskyblue")
        c.create_polygon((350, 150), (450, 250), (350, 350), (250, 250),  fill="deepskyblue", outline="deepskyblue")
        c.create_polygon((425, 100), (525, 200), (425, 300), (325, 200),  fill="deepskyblue", outline="deepskyblue")

        a = Canvas(window2, width=550, height=400, bg='white')
        a.create_polygon((350, 50), (450, 150), (350, 250), (250, 150), fill="", outline="red", width=3)
        a.create_polygon((275, 100), (375, 200), (275, 300), (175, 200), fill="", outline="orange", width=3)
        a.create_polygon((350, 150), (450, 250), (350, 350), (250, 250), fill="", outline="lime", width=3)
        a.create_polygon((425, 100), (525, 200), (425, 300), (325, 200), fill="", outline="deepskyblue", width=3)

        b = Canvas(window2, width=550, height=400, bg='white')
        b.create_polygon((350, 50), (450, 150), (350, 250), (250, 150), fill="red", outline="")
        b.create_polygon((275, 100), (375, 200), (275, 300), (175, 200), fill="orange", outline="")
        b.create_polygon((350, 150), (450, 250), (350, 350), (250, 250), fill="lime", outline="")
        b.create_polygon((425, 100), (525, 200), (425, 300), (325, 200), fill="deepskyblue", outline="")

        d = Canvas(window2, width=550, height=400, bg='white')
        d.create_polygon((350, 50), (450, 150), (350, 250), (250, 150), fill="red", outline="darkred", width=7)
        d.create_polygon((275, 100), (375, 200), (275, 300), (175, 200), fill="orange", outline="darkorange", width=7)
        d.create_polygon((350, 150), (450, 250), (350, 350), (250, 250), fill="lime", outline="green", width=7)
        d.create_polygon((425, 100), (525, 200), (425, 300), (325, 200), fill="deepskyblue", outline="blue", width=7)
        c.grid(row=1, column=1)
        a.grid(row=1, column=2)
        b.grid(row=2, column=1)
        d.grid(row=2, column=2)

    else:
        window2.destroy()
        window2 = None


def task3_def():
    global window3
    if window3 == None:
        window3 = Toplevel()

        c = Canvas(window3, width=700, height=200, bg='white')
        a = 26
        points1 = []
        c.create_line(100, 100, 697, 100, width=3, fill="black", arrow="last")
        c.create_line(415, 200, 415, 3, width=3, fill="black", arrow="last")
        for x in range(500):
            y = 3*0.01*26*math.sin(-x)
            points1.append(tuple([x*50+100, y*50+100]))
        c.create_line(points1, fill="red", smooth=1, width=3)

        b = Canvas(window3, width=700, height=200, bg='white')
        a = 26
        points2 = []
        b.create_line(100, 100, 697, 100, width=3, fill="black", arrow="last")
        b.create_line(415, 200, 415, 3, width=3, fill="black", arrow="last")
        for x in range(500):
            y = 3 * 0.01 * 26 * math.cos(-x)
            points2.append(tuple([x * 50 + 100, y * 50 + 100]))
        b.create_line(points2, fill="lime", smooth=1, width=3)

        d = Canvas(window3, width=700, height=200, bg='white')
        a = 26
        points3_1 = []
        points3_2 = []
        points3_3 = []
        points3_4 = []
        d.create_line(100, 100, 697, 100, width=3, fill="black", arrow="last")
        d.create_line(415, 200, 415, 3, width=3, fill="black", arrow="last")
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        f1 = 0
        while f1<math.pi/2:
            list1.append(f1)
            f1 += 0.1
        for x in list1:
            y = 3 * 0.01 * 26 * math.tan(-x)
            points3_1.append(tuple([x * 50 + 100, y * 50 + 100]))
        d.create_line(points3_1, fill="orange", smooth=1, width=3)

        f2 = math.pi/2 + 0.1
        while f2<3*math.pi/2:
            list2.append(f2)
            f2 += 0.1
        for x in list2:
            y = 3 * 0.01 * 26 * math.tan(-x)
            points3_2.append(tuple([x * 50 + 100, y * 50 + 100]))
        d.create_line(points3_2, fill="orange", smooth=1, width=3)

        f3 = 3*math.pi / 2 + 0.1
        while f3 < 5 * math.pi / 2:
            list3.append(f3)
            f3 += 0.1
        for x in list3:
            y = 3 * 0.01 * 26 * math.tan(-x)
            points3_3.append(tuple([x * 50 + 100, y * 50 + 100]))
        d.create_line(points3_3, fill="orange", smooth=1, width=3)
        f4 = 5 * math.pi / 2 + 0.1
        while f4 < 7 * math.pi / 2:
            list4.append(f4)
            f4 += 0.1
        for x in list4:
            y = 3 * 0.01 * 26 * math.tan(-x)
            points3_4.append(tuple([x * 50 + 100, y * 50 + 100]))
        d.create_line(points3_4, fill="orange", smooth=1, width=3)

        # eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee

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


        a = 26
        points3_1 = []
        points3_2 = []
        points3_3 = []
        points3_4 = []
        e.create_line(100, 100, 697, 100, width=3, fill="black", arrow="last")
        e.create_line(415, 200, 415, 3, width=3, fill="black", arrow="last")
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
        e.create_line(points3_1, fill="orange", smooth=1, width=3)

        f2 = math.pi / 2 + 0.1
        while f2 < 3 * math.pi / 2:
            list2.append(f2)
            f2 += 0.1
        for x in list2:
            y = 3 * 0.01 * 26 * math.tan(-x)
            points3_2.append(tuple([x * 50 + 100, y * 50 + 100]))
        e.create_line(points3_2, fill="orange", smooth=1, width=3)

        f3 = 3 * math.pi / 2 + 0.1
        while f3 < 5 * math.pi / 2:
            list3.append(f3)
            f3 += 0.1
        for x in list3:
            y = 3 * 0.01 * 26 * math.tan(-x)
            points3_3.append(tuple([x * 50 + 100, y * 50 + 100]))
        e.create_line(points3_3, fill="orange", smooth=1, width=3)
        f4 = 5 * math.pi / 2 + 0.1
        while f4 < 7 * math.pi / 2:
            list4.append(f4)
            f4 += 0.1
        for x in list4:
            y = 3 * 0.01 * 26 * math.tan(-x)
            points3_4.append(tuple([x * 50 + 100, y * 50 + 100]))
        e.create_line(points3_4, fill="orange", smooth=1, width=3)

        c.create_text(697, 90, text="X", fill="grey")
        c.create_text(425, 15, text="Y", fill="grey")
        d.create_text(697, 90, text="X", fill="grey")
        d.create_text(425, 15, text="Y", fill="grey")
        b.create_text(697, 90, text="X", fill="grey")
        b.create_text(425, 15, text="Y", fill="grey")
        e.create_text(697, 90, text="X", fill="grey")
        e.create_text(425, 15, text="Y", fill="grey")

        c.grid(row=1, column=1)
        e.grid(row=2, column=2)
        b.grid(row=2, column=1)
        d.grid(row=1, column=2)
    else:
        window3.destroy()
        window3 = None


task1_button = Button(root, text="Завдання 1", command=task1_def)
task2_button = Button(root, text="Завдання 2", command=task2_def)
task3_button = Button(root, text="Завдання 3", command=task3_def)

window1 = None
window2 = None
window3 = None

task1_button.pack()
task2_button.pack()
task3_button.pack()
root.mainloop()