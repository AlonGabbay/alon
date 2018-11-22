from sympy import *
import cmath
import numpy as np
def func(symbolic_fuction):
    return lambdify(x, symbolic_fuction, 'numpy')

def find_roots(rangex):
    intervals = []
    j = rangex[0]
    for _ in range((abs(rangex[1])+abs(rangex[0])) * 2):
        intervals.append([j, j + 0.5])
        j = j + 0.5
    return intervals

def secant(rangex, fx, x0, x1, eps, itration):
    while abs(x1 - x0) > eps or itration == 0:
        if fx(x1) - fx(x0) == 0:
            return None
        x = x1 - fx(x1) * ((x1 - x0)/(fx(x1) - fx(x0)))
        x0 = x1
        x1 = x
        itration -= 1
    return x

def all_roots(fx, eps, rangex, itration):
    roots = []
    k = 0
    almostE=0.01
    intervals = find_roots(rangex)
    for i in intervals:
        x0 = (i[0] + i[1]) / 3
        x1 = (i[0] + i[1]) / 2
        temp = secant(rangex, fx, x0, x1, eps, itration)

        if temp != None:
            if(len(roots)==0):
                if temp >= rangex[0] and temp <= rangex[1]:
                    roots.append(temp)
            else:
                if temp >= roots[k]-almostE and roots[k]+almostE >=temp:
                    continue
                if temp <= rangex[1] and temp >= rangex[0]:
                       roots.append(temp)
                       k = k + 1
    if len(roots) == 0:
        return None
    return roots

if __name__ == '__main__':
    x = Symbol('x')
    gx = ln(x) ** 2
    fx = func(gx)
    print(all_roots(fx, 0.0001, [0,3], 100))

