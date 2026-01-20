import math

# Iteration function
def g(x):
    return ((2*x + 5) / 2) ** (1/3)

def fixed_point_iteration(x0, tolerance=0.00001, max_iter=100):
    for i in range(max_iter):
        x1 = g(x0)
        if abs(x1 - x0) < tolerance:
            print("First approximate root =", format(x1, ".4f"))
            return
        x0 = x1

    print("Method did not converge")

# Initial guess
x0 = 2
fixed_point_iteration(x0)
