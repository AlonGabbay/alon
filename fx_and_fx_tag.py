from sympy import *
import cmath
import numpy as np
def func(symbolic_fuction):
    return lambdify(x, symbolic_fuction, 'numpy')

def derivative(symbolic_fuction):
    g_tagx = diff(symbolic_fuction)
    return lambdify(x, g_tagx, 'numpy')


if __name__ == '__main__':
    x = Symbol('x')
    fx = cos(x)
    gx = func(fx)
    fx_tag = derivative(fx)

    print(gx(1))
    print(fx_tag(1))
