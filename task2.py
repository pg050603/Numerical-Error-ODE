import numpy as np
from module_lab5 import *
from scipy.integrate import solve_ivp

#Set up solve_ivp inputs
a = solve_ivp(derivative_ode1, [0, 2], [4])

#Calculate exact y values of t using exact solution function, remove initial condition
y_exact = exact_solution_ode1(a.t)[1:]

#Convert approximate y values into list type and remove initial condition
y_approx = np.ndarray.tolist(a.y[0])[1:]

#Calculate mean absolute error between the exact and approximate
mae = mean_absolute_error(y_exact, y_approx)

# Convert t values into list type and remove initial condition
t = list(a.t)[1:]

print(mae)
print(y_exact)
print(y_approx)


#Create figure
plt.figure(figsize=(5,2.7), layout = 'constrained')
#Plot the approx y values against t from SOLVE_IVP, excluding initial condition
plt.plot(t, y_approx, label='y_approx')
#Plot the exact y values against t, excluding initial condition
plt.plot(t, y_exact, label='y_exact')
#Axis lables, title, and legend
plt.xlabel('Time (t)')
plt.ylabel('y')
plt.title("y_approx and y_exact against t")
plt.legend()

plt.show()

