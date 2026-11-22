import numpy as np

def psi(x):
    return np.exp(- x ** 2 / 2)

def FDS2(f, x, h):
    return (f(x + 2 * h) - 2 * f(x + h) + f(x)) / h ** 2

def BDS2(f, x, h):
    return (f(x) - 2 * f(x - h) + f(x - 2 * h)) / h ** 2

def CDS2(f, x, h):
    return (2 * f(x) - 2 * (f(x + h) + f(x - h)) + f(x + 2 * h) + f(x - 2 * h)) / (2 * h ** 2)

x = 0.5
exact = (x ** 2 - 1) * np.exp(- x ** 2 / 2)

for h in [0.001, 0.01, 0.05, 0.1, 0.25, 0.5]:
    print(" ")
    print("h:", h)

    FDS_result = FDS2(psi, x, h)
    print("FDS:", FDS_result)
    print("FDS error:", FDS_result - exact)

    BDS_result = BDS2(psi, x, h)
    print("BDS:", BDS_result)
    print("BDS error:", BDS_result - exact)

    CDS_result = CDS2(psi, x, h)
    print("CDS:", CDS_result)
    print("CDS error:", CDS_result - exact)