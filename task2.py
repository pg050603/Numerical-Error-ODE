import numpy as np

from module_lab5 import *
from scipy.integrate import solve_ivp

#Set up solve_ivp inputs
a = solve_ivp(derivative_ode1, [0, 2], [4])

print(a)

print(a.t)
print(a.y)


# use Mean error to find error
pass
