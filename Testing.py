import numpy as np
import matplotlib.pyplot as plt

gamma = [[1,2,3], [4,5,6], [7,8,9]]

f =


print(gamma)
# a = len(gamma)
# print(a)

for i in range(len(gamma)):
    gamma_row = gamma[i][:]
    for j in range(len(gamma_row)):
        print(gamma_row[j])


#kn1 = f(tn, yn)
#kn2 = f(tn + Bih, yn + gammaij * h * kn1)
#kn3 = f(tn + Bih, yn + gammaij * h * kn2)
#kn4 = f(tn + Bih, yn + gammaij * h * kn3)

#For this case:
#kn1 = f(tn, yn)
#kn2 = f(tn + 0.5h, yn + 0.5h * kn1)
#kn3 = f(tn + 0.5h, yn + 0.5h * kn2)
#kn4 = f(tn + h, yn + h * kn3)

# => yn+1 = yn + h/6(kn1 + 2kn2 + 2kn3 + kn4)