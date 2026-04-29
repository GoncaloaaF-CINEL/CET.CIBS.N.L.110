from math import sqrt
import re

def soma(num1, num2):
    return num1 + num2



def fresolv(a: float, b: float, c: float) -> tuple[float, float]:

    delta = pow(b, 2) - 4 * a * c

    if delta < 0:
        return "impossible"

    raiz = sqrt(delta)

    x1 = (-b + raiz) / (2 * a)
    x2 = (-b - raiz) / (2 * a)

    return x1, x2


def idIpValid(ip:str) -> bool:
    x = re.search("^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$", ip)
    return True if x else False

