from sympy import *
import scipy as sp
import numpy as np
import matplotlib.pylab as plt

def f(list):
    '''
    :param list: list of coefficients
    :type list: list []
    :return: polynomial function as lambda
    '''
    return lambda x : list[0]*x**6 + list[1]*x**5 + list[2]*x**4 + list[3]*x**3 + list[4]*x**2 + list[5]*x + list[6]

def g(list):
    '''
    :param list: list of coefficients
    :return: polynomial function
    '''
    return list[0]*x**6 + list[1]*x**5 + list[2]*x**4 + list[3]*x**3 + list[4]*x**2 + list[5]*x + list[6]

def bisection(a, b, iteration, function, epsilon):
    '''
    :param a: start index
    :type a: float
    :param b: end index
    :type b: float
    :param iteration: amount of iterations
    :type iteration: int
    :param function: Polynomial function
    :type function: lambda x: polynom result
    :param epsilon: exceptable exception
    :type epsilon: float
    :return: root of function or "none"
    '''
    if function(a) * function(b) <= 0 :
        c = (a + b) / 2
        while((b - a) > epsilon or iteration == 0 ) :
            if(function(a) == 0):
                return a
            if(function(b) == 0):
                return b
            if(function(c) == 0):
                return c
            elif(function(a) * function(c) > 0):
                a = c
            elif(function(c) * function(b) > 0):
                b = c
            iteration = iteration - 1
            c = (a + b) / 2
        return c
    else:
        return "none"

def exponentIndex(list):
    '''
    :param list: List of coefficients
    :type list: list []
    :return: highest exponent of function
    '''
    for i in range(7):
        if(not(list[i] == 0)):
                return 6 - i

def derivative(func, x):
    '''
    :param func: polynomial function
    :type func: function
    :param x: input of diff function
    :type x: symbol
    :return: derivative of func function
    '''

    func_tag = diff(func, x, 1)
    return func_tag
    #lambdify(x, func_tag, 'numpy')


def roots(ranging, expo, function, iteration, epsilon):
    '''
    :param ranging: coordinates of seagmants a,b
    :param expo: highest exponent of function
    :param function: Polynomial function
    :param iteration: number of iteration
    :param epsilon:exceptable exception
    :return: List of roots
    '''
    count = 0
    j = 0
    rootList = []
    for k in ranging:
        if( j == len(ranging) - 1):#if j gets to the end of the list - 1
            return rootList
        tmp = bisection(ranging[j], ranging[j + 1], iteration, function, epsilon)
        if (not(tmp == "none")):
            if(len(rootList) > 0):
                if(tmp + 2 * epsilon >= rootList[count - 1]  or tmp - 2 * epsilon<= rootList[count - 1] ):
                    count = count + 1
                    rootList.append(tmp)
            else:
                count = count + 1
                rootList.append(tmp)
        if (count == expo):
            return rootList
        j = j + 1

    return rootList

if __name__ == '__main__':

    epsilon = 0.001
    iteration = 100
    Start_Domain = -10
    interval_jump = 0.5

    count = 0
    rootList = []
    ranging = []

    #Definition of domain
    End_Domain = -Start_Domain
    parameter = Start_Domain
    tmp = (-2 * Start_Domain) / interval_jump #Do you not understand? ok, ask Alon!
    for i in range(int(tmp)):
        ranging.append(parameter)
        parameter += interval_jump

    #Function coefficients input from the user
    print("Enter the polinomyal parameters from x^6 to x^0, 7 parameters:")
    fxParameters = [float(z) for z in input().split()]
    expo = exponentIndex(fxParameters)
    function = f(fxParameters)

    #List of roots
    rootList = roots(ranging, expo, function, iteration, epsilon)
    print(set(rootList))

    x = Symbol('x')
    function = g(fxParameters)

    z = derivative(function, x)
    function = z
    b = derivative(function, x).as_content_primitive(True)
    c =lambdify(x,b[1], 'numpy')
    print(c(1))


    try:
        if type(b) == str:
            print("it is")
        else:
            print("b is not a string, b is a: ",type(b))
    except: TypeError:\
        print("Error")


    #eval("b")(1)
    #lambdify(x, b, 'numpy')
    print(b)
    '''
    t = bisection(-1.5, -1, iteration, function, epsilon)
    print(t)
    
    t = np.arange(Start_Domain, End_Domain, 0.01)
    plt.plot(ranging, function,lw = 2)
    #plt.axis([Start_Domain,End_Domain,-20,20])
    plt.show()
    '''


