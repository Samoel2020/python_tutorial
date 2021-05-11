"""
import matplotlib.pyplot as plt
def abline():
    gca = plt.gca()
    gca.set_autoscale_on(False)
    gca.plot(gca.get_xlim(),gca.get_ylim())


plt.scatter(range(10),range(10))
abline()
plt.draw()
plt.show()
"""
# import numpy as np
# import matplotlib.pyplot as plt

x_intercept = 3  # invented x coordinate
y_intercept = 2  # invented y coordinate
my_slope = 1  # invented slope value

def find_second_point(slope,x0,y0):
    # this function returns a point which belongs to the line that has the slope 
    # inserted by the user and that intercepts the point (x0,y0) inserted by the user
    q = y0 - (slope*x0)  # calculate q
    new_x = x0 + 10  # generate random x adding 10 to the intersect x coordinate
    new_y = (slope*new_x) + q  # calculate new y corresponding to random new_x created

    return new_x, new_y  # return x and y of new point that belongs to the line

# invoke function to calculate the new point
new_x, new_y = find_second_point(my_slope , x_intercept, y_intercept)
print(new_x, new_y)









