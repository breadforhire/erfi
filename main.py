from sympy import *
import math
import numpy as np
import scipy
from mpmath import mp


np.set_printoptions(precision=1)
np.set_printoptions(threshold = np.inf)
np.set_printoptions(suppress=False)

n = 1000
CONST = n / (math.sqrt((math.pi) * n))


# without vectorization
def erfi(n):
    result = 0
    n += 1
    for x in range (n):
     result += factorial((2 * n) - 1) / ((2 * n ** 2) ** n)
     print(f"{result * CONST} \n")


def vector(n):
 n += 1
 erfi_mul = np.full(n, CONST)
 li = np.arange(1, n + 1)

 result = (scipy.special.factorial((2 * li) - 1) / ((2 * li ** 2) ** li)) * erfi_mul
 #result = np.ma.masked_invalid(result)
 print(result)






#erfi(n)

vector(n)
