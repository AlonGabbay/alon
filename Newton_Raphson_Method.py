from sympy import *
import cmath
import numpy as np
def func(symbolic_fuction):
    return lambdify(x, symbolic_fuction, 'numpy')

def derivative(symbolic_fuction):
    g_tagx = diff(symbolic_fuction)
    return lambdify(x, g_tagx, 'numpy')

def find_roots(rangex):
    intervals = []
    j = rangex[0]
    for _ in range((abs(rangex[1])+abs(rangex[0])) * 2):
        intervals.append([j, j + 0.5])
        j = j + 0.5
    return intervals


def NR(f, f_tag, x,eps, itration):
    while abs(f(x)) > eps or itration == 0:
        if f_tag(x) == 0:
            return None
        x = x - f(x) / f_tag(x)
        itration -= 1
    return x
def all_roots(f, f_tag, eps, rangex, itration):
    roots = []
    k = 0
    almostE=0.01
    intervals = find_roots(rangex)
    for i in intervals:
        x = (i[0] + i[1]) / 2
        if NR(f, f_tag, x,eps, itration) != None:
            if(len(roots)==0)and NR(f, f_tag, x,eps, itration <= rangex[1]) and NR(f, f_tag, x,eps, itration >= rangex[0]):
                roots.append(NR(f, f_tag, x, eps, itration))
            else:
                temp = NR(f, f_tag, x, eps, itration)
                if temp == None:
                    continue
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
    gx = cos(x)
    fx = func(gx)
    print(fx(0))
    fx_tag = derivative(gx)
    print(all_roots(fx, fx_tag, 0.00001, [0,3], 100))

