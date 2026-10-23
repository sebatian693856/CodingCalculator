from curses import window
import math

import numpy as np
print(np.__version__)
import scipy 
from scipy.special import jv, jve, yn, yv, yve, iv, ive, kn, kv, kve
print(scipy.__version__)

e = math.e

function = str(input("Function - Eg:  +, -, *, /, sinh, cosh, tanh, sech, csch, coth, Bessel1 to Bessel10:"))
x = float(input("Number:"))

if function == "sinh":
    ans = math.sinh(x)
    print(ans)
elif function == "cosh":
    ans = math.cosh(x)
    print(ans)
elif function == "tanh":
    ans = math.tanh(x)
    print(ans)
elif function == "sech":
    var1 = e ** x
    var2 = e ** (-x)
    ans = 2 / (var1 + var2)
    print(ans)
elif function == "csch":
    ans = 2 / (e ** x - e ** (-x))
    print(ans)
elif function == "coth":
    var1 = e ** x
    var2 = e ** (-x)
    ans = (var1 + var2) / (var1 - var2)
    print(ans)

elif function in ["+", "-", "*", "/", "Bessel1", "Bessel2", "Bessel3", "Bessel4", "Bessel5", "Bessel6", "Bessel7", "Bessel8", "Bessel9", "Bessel10"]:
    y = float(input("Second Number (y): "))
    if function == "+":
       ans = x + y
       print(ans)
    elif function == "*":
        ans = x * y
        print(ans)
    elif function == "-":
        ans = x - y
        print(ans)
    elif function == "/":
        ans = x / y
        print(ans)
    elif function == "Bessel1":
        ans = jv(x, y)
        print(ans)
    elif function == "Bessel2":
        ans = jve(x, y)
        print(ans)
    elif function == "Bessel3":
        ans = yn(int(x), y)
        print(ans)
    elif function == "Bessel4":
        ans = yv(x, y)
        print(ans)
    elif function == "Bessel5":
        ans = yve(x, y)
        print(ans)
    elif function == "Bessel6":
        ans = iv(x, y)
        print(ans)
    elif function == "Bessel7":
        ans = ive(x, y)
        print(ans)
    elif function == "Bessel8":
        ans = kn(int(x), y)
        print(ans)
    elif function == "Bessel9":
        ans = kv(x, y)
        print(ans)
    elif function == "Bessel10":
        ans = kve(x, y)
        print(ans)

import turtle

x = 10

t = turtle.Turtle()
window.bgcolor("black")


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

def drawpoint():
    t.right(90)
    t.forward(17)
    t.pendown()
    t.forward(3)
    t.penup()
    t.back(20)
    t.left(90)
    t.forward(20)
def drawminus():
    t.pendown()
    t.forward(10)
    t.penup()
    t.forward(20)
def drawe():
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
    t.penup()
    t.forward(20)
    t.right(90)
    t.forward(20)



def drawplus():
    t.pendown()
    t.forward(40)
    t.back(20)
    t.left(90)
    t.forward(20)
    t.back(40)
    t.forward(20)
    t.right(90)
    t.penup()
    t.forward(40)




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
        drawminus()
    elif digit == ".":
        drawpoint()
    elif digit == "e":
        drawe()
    elif digit == "+":
        drawplus()


def test4():
    text = str(ans)
    for ch in text:
        draw_digit(ch)

test4()

t.done()
