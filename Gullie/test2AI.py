import turtle

# Example value for ans
ans = 99.4

window = turtle.Screen()
window.bgcolor("black")
window.title("Number Printer")

t = turtle.Turtle()
t.speed(0)
t.color("green")
t.hideturtle()

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

def draw9():
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

def draw_minus():
    t.pendown()
    t.forward(20)
    t.penup()
    t.forward(20)

def draw_decimal():
    t.pendown()
    t.forward(2)
    t.penup()
    t.forward(12)

def draw_digit(digit):
    if digit == "0":
        draw0()
    elif digit == "1":
        draw1()
    elif digit == "2":
        draw2()
    elif digit == "3":
        draw3()
    elif digit == "4":
        draw4()
    elif digit == "5":
        draw5()
    elif digit == "6":
        draw6()
    elif digit == "7":
        draw7()
    elif digit == "8":
        draw8()
    elif digit == "9":
        draw9()
    elif digit == "-":
        draw_minus()
    elif digit == ".":
        draw_decimal()

def test4():
    text = str(ans)
    for ch in text:
        draw_digit(ch)
        t.penup()
        t.forward(30)
        t.pendown()

test4()

window.exitonclick()
