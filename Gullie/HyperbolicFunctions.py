import math

import numpy as np
print(np.__version__)
import scipy 
from scipy.special import jv, jve, yn, yv, yve, iv, ive, kn, kv, kve
print(scipy.__version__)

e = math.e

function = str(input("Function - Eg:  +, -, *, /, sinh, cosh, tanh, sech, csch, coth, Bessel1, Bessel2:"))
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
