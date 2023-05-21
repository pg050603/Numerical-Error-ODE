# import statements
import numpy as np
import matplotlib.pyplot as plt
import math


def difference_squares(x, y):
    """ TODO
    Calculates the difference between squares of inputs x & y using two methods and displays difference to 32 d.p.
    Arugements:
    ----------
    x float: Input number 1
    y float: Input number 2
    """
    # Calculate difference between squares using method 1
    z1 = x ** 2 - y ** 2
    # Calculate difference between squares using method 2
    z2 = (x - y) * (x + y)
    # Print results to screen to 32 d.p.
    print(f'The value of z1 to 32 d.p. is: {z1:.32f}')
    print(f'The value of z2 to 32 d.p. is: {z2:.32f}')

    pass


def relative_error_subtraction(x, y, z_exact):
    """ TODO
    Calculates the difference between values x and y
    Compares to exact difference

    Arguements:
    -----------
    x float: Input 1
    y float: Input 2
    z_exact float: Exact value of difference (z = x - y)
    """
    # Compute the approximate value of z
    z = x - y
    # Calculate the relative error between z and z exact
    error = z_exact - z
    # Print x, y, z, z_exact to 64 d.p. and the relative error to 16 d.p.
    print(f'The value of x to 64 d.p. is: {x:.64f}')
    print(f'The value of y to 64 d.p. is: {y:.64f}')
    print(f'The approximate value of z to 64 d.p. is: {z:.64f}')
    print(f'The exact value of z to 64 d.p. is: {z_exact:.64f}')
    print(f'The relative error between z_exact and z to 16 d.p. is: {error:.16f}')

    pass


def exact_solution_ode1(t):
    """ TODO
        calculates exact solution to the ODE y' + 5y = 2e^-5t

        Arguements:
        -----------
        t Float or array like: Independent variable

        Returns:
        -------
        y_exact Float or array-like: Exact ODE solution for t
        """
    # If t is a float, get single solution
    if type(t) == float:
        y_exact = math.exp(-5 * t) * (2 * t + 4)
    # If t is a list, determine ODE solution for every t value
    elif type(t) == list or type(t) == np.ndarray:
        # Initialise storage list to limit computational drag
        y_exact = [0] * len(t)
        # y_exact = exact_solution_ode1(t)
        for i in range(len(t)):
            y_exact[i] = math.exp(-5 * t[i]) * (2 * t[i] + 4)
    return y_exact


def mean_absolute_error(y_exact, y_approx):
    """ TODO
    calculate the mean absolute error for an approximate solution.

    Arguements:
    ----------
    y_exact 1D Numpy array: Exact solutions
    y_approx 1D Numpy array: Numerically approximated solution

    Returns:
    --------
    mae Float: The mean absolute error in numerical solution

    Notes:
    ------
    y_exact and y_approx have the same length
    """
    difference = 0
    n = len(y_exact)
    for i in range(n):
        element_diff = difference + abs(y_exact[i] - y_approx[i])
    mae = element_diff / n
    return mae



def derivative_ode1(t, y):
    """
    Used to calculate dy/dt for ODE

    Arugements:
    ----------
    t float: Value of indepedent variable
    y float: Value of dependent variable

    Returns:
    --------
    dydt float: Value of first-order derivative
    """

    dydt = 2 * math.exp(-5 * t) - 5 * y

    return dydt



def euler_step(f, t, y, h):
    """
    Calculate one step of the Euler method.

    Parameters
    ----------
    f : function
        Derivative function (callable).
    t : float
        Independent variable at start of step.
    y : float
        Dependent variable at start of step.
    h : float
        Step size along independent variable.

    Returns
    -------
    y_new : float
        Dependent variable at end of step.
    """
    f0 = f(t, y)
    y_new = y + h * f0
    return y_new


def improved_euler_step(f, t, y, h):
    """
    Calculate one step of the Improved Euler method.

    Parameters
    ----------
    f : function
        Derivative function (callable).
    t : float
        Independent variable at start of step.
    y : float
        Dependent variable at start of step.
    h : float
        Step size along independent variable.

    Returns
    -------
    y_new : float
        Dependent variable at end of step.
    """
    f0 = f(t, y)
    f1 = f(t + h, y + h * f0)
    y_new = y + h * 0.5 * (f0 + f1)
    return y_new


def classic_rk4_step(f, t, y, h):
    """
    Calculate one step of the Classic RK4 method.

    Parameters
    ----------
    f : function
        Derivative function (callable).
    t : float
        Independent variable at start of step.
    y : float
        Dependent variable at start of step.
    h : float
        Step size along independent variable.

    Returns
    -------
    y_new : float
        Dependent variable at end of step.
    """
    f0 = f(t, y)
    f1 = f(t + h * 0.5, y + h * 0.5 * f0)
    f2 = f(t + h * 0.5, y + h * 0.5 * f1)
    f3 = f(t + h, y + h * f2)
    y_new = y + h * (f0 + 2. * f1 + 2. * f2 + f3) / 6.
    return y_new


def explicit_rk_step(f, t, y, h, alpha, beta, gamma):
    """ TODO
        Performs one step of an explicit RK method based on its Butcher tableau.

        Arguements:
        -----------
        f (function): Function that is called to return first order ODE
        t float: Value of independent variable at start of step
        y float: Value of dependent variable start of step
        h float: Step size along t
        alpha 1D np array: Weights from Butcher tables
        beta 1D np array: Nodes from butcher tables
        gamma 2D np array: RK matrix from butcher tables

        Returns:
        --------
        y_new float: value of dependent variable at end of step
        """
#     i = 0
#     for *condition *:
#         gamma_row = gamma[i][:]
#         for *condition *:
#             f_i = f(t + beta[j] * h, y + h * gamma_row[j] *)
#
#
# row
# of
# gamma
# dot
# product
# with f array
#
# f
# array
# starts
# all
# 0
# f[0]
# set in the
# first
# iteration
# f2
# uses
# f1 and is then
# calculated in that
# iterations
# f3
# uses
# f1 and f2
# then
# calculates
#
# y_new = y + h * a
#
# return y_new
#
# pass


def explicit_rk_solver(f, tspan, y0, h, alpha, beta, gamma):
    """ TODO
    """
    pass
