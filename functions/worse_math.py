import math

def frange(lowerlim=-10*math.pi, upperlim=10*math.pi, step=0.1):
    n_elements= round((upperlim-lowerlim)*(1/step))
    better_array= []
    n=0

    while n < n_elements:
        if n == 0:
            better_array.append(lowerlim+step)
        else:
            better_array.append(round(better_array[n-1]+step,2))
        n+=1

    return better_array


def slope_finder(x, function, step = 0.001):
    y1 = eval(function)
    x = x + step
    y2= eval(function)
    slope= (y2-y1)/(step)
    return round(slope,6)

