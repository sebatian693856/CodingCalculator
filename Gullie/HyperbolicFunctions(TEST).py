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
    print(math.sinh(x))
elif function == "cosh":
    print(math.cosh(x))
elif function == "tanh":
    print(math.tanh(x))
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
       print(x + y)
       ans = x + y
    elif function == "*":
        print(x * y)
        ans = x * y
    elif function == "-":
        print(x - y)
        ans = x - y
    elif function == "/":
        print(x / y)
        ans = x / y
    elif function == "Bessel1":
        print(jv(x, y))
    elif function == "Bessel2":
        print(jve(x, y))
    elif function == "Bessel3":
        print(yn(int(x), y))
    elif function == "Bessel4":
        print(yv(x, y))
    elif function == "Bessel5":
        print(yve(x, y))
    elif function == "Bessel6":
        print(iv(x, y))
    elif function == "Bessel7":
        print(ive(x, y))
    elif function == "Bessel8":
        print(kn(int(x), y))
    elif function == "Bessel9":
        print(kv(x, y))
    elif function == "Bessel10":
        print(kve(x, y))


