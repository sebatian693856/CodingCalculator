import turtle

x = 10

t = turtle.Turtle()

t.speed(5)
t.color("green")

t.penup()
t.forward(600)
t.pendown()
t.left(90)
t.forward(270)
t.left(90)
t.forward(1200)
t.left(90)
t.forward(540)
t.left(90)
t.forward(1200)
t.left(90)
t.forward(270)
t.penup()
t.left(90)
t.forward(1160)
t.right(90)
t.forward(220)
t.right(90)
t.pendown()

def draw0():
    t.pendown()
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.penup()
    t.forward(40)

def draw1():
    t.pendown()
    t.left(90)
    t.forward(20)
    t.back(40)
    t.forward(20)
    t.right(90)
    t.penup()
    t.forward(20)

def draw2():
    t.pendown()
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.penup()
    t.forward(20)
    t.pendown()
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.penup()
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)

def draw3():
    t.pendown()
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.penup()
    t.forward(40)
    t.pendown()
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.penup()
    t.forward(20)

def draw4():
    t.pendown()
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.penup()
    t.forward(20)
    t.left(90)
    t.pendown()
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.back(20)
    t.left(90)
    t.penup()
    t.forward(20)

def draw5():
    t.pendown()
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.penup()
    t.right(90)
    t.forward(20)
    t.pendown()
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.penup()
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(20)

def draw6():
    t.pendown()
    x = 0
    while x <= 3:
        t.forward(20)
        t.right(90)
        x = x + 1
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.penup()
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(20)

def draw7():
    t.left(90)
    t.penup()
    t.forward(20)
    t.pendown()
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(40)
    t.penup()
    t.back(20)
    t.left(90)
    t.forward(20)

def draw8():
    t.pendown()
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.penup()
    t.forward(20)

def  draw9():
    t.pendown()
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.penup()
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.pendown()
    t.left(90)
    t.forward(20)
    t.right(90)
    t.penup()
    t.forward(20)

num1 = int(input(""))


def num_make1():
    if num1 == 0:
       draw0()
    elif num1 == 1:
        draw1()
    elif num1 == 2:
        draw2()
    elif num1 == 3:
        draw3()
    elif num1 == 4:
        draw4()
    elif num1 == 5:
        draw5()
    elif num1 == 6:
        draw6()
    elif num1 == 7:
        draw7()
    elif num1 == 8:
        draw8()
    else:
        draw9()

num1 = int(input(""))


def num_make1():
    if num1 == 0:
       draw0()
    elif num1 == 1:
        draw1()
    elif num1 == 2:
        draw2()
    elif num1 == 3:
        draw3()
    elif num1 == 4:
        draw4()
    elif num1 == 5:
        draw5()
    elif num1 == 6:
        draw6()
    elif num1 == 7:
        draw7()
    elif num1 == 8:
        draw8()
    else:
        draw9()



while 9 > 1:
    t.speed(0.5)
    t.penup()
    t.forward(2)
    t.back(2)
