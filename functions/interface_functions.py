import sys, math, numpy as np
import matplotlib.pyplot as plt
from functions import worse_math

def domain():
    y= input("Use default domain? (Y/N): ")
    if y.lower() == 'y':
        domain= worse_math.frange()
    elif y.lower() == 'n':
        lower_bound, upper_bound, step= input("Define the domain in python readable terms with step: ").split(" ")    
        domain = worse_math.frange(eval(lower_bound), eval(upper_bound), float(step))
    else:
        print("Invalid input")
    return domain

def function_creator():
    boo= input("Is your function simple or composite? (S/C): ")
    if boo.lower() == "s":
        fin= input("Enter Function: ")
        function= f"math.{fin}(x)"
    elif boo.lower() == "c":
        function= input("Enter Function in python readable form: ")
    else:
        print("Invalid input")
    return function

def slope_finding_interface(function):
    boo= input("Would you like to find slope at a point? (Y/N): ")
    if boo.lower() == 'y':
        x = float(input("Enter x at which slope is to be found: "))
        print(worse_math.slope_finder(x, function))
    elif boo.lower() == 'n':
        sys.exit()
    else:
        print("Invalid input")

def grapher(domain, function):
    ypoints= np.array([eval(function) for x in domain])
    xpoints= np.array([x for x in domain])
    plt.plot(xpoints, ypoints)
    plt.show()
    return