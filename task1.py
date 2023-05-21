from module_lab5 import *

#Task 1a Function Call
difference_squares(1 + 2**-29, 1 + 2**-30)

#Task 1b function call
x = 1 + math.exp(1) - 15
y = 1 + 2 * math.exp(1) - 15
z_exact = -1*math.exp(1)

relative_error_subtraction(x, y, z_exact)


print(-0.0000000000000004/-2.7182818284590450907955982984276488423347473144531250000000000000)



# a = 1 + math.exp(1) - 15
# b = 1 + math.exp(2) - 15
# diff = b - a
# relative_error_subtraction(a, b, diff)



pass
