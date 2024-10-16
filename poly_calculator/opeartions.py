import math
import re

def add(x: float, y: float) -> float:
    return x + y

def sub(x: float, y: float) -> float:
    return x - y

def mult(x: float, y: float) -> float:
    return x * y

def div(x: float, y: float) -> float:
    if y == 0:
        raise ValueError("Can't divide by 0")
    return x / y

def exp(x: float, y: float) -> float:
    return x ** y

def poly_deriv(expression: str) -> str:
    f_x = re.split(r'([+-])', expression)
    result = []
    for item in f_x:
        if("x^" in item or "x" in item):
            value = item.split("x^")
            base = float(value[0])
            exp = float(value[1])
            result.append(str(base * exp) + "x^" + str(exp - 1))
        else:   
            result.append(item)
            
    return ''.join(result)