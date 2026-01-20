# Fixed Point Iteration Method

import math

def g(x):
    return ((2*x + 5) / 2) ** (1/3)

def iteration_method(x0, tolerance=0.0001, max_iter=100):
    print("Iteration\tValue of x")
    
    for i in range(1, max_iter + 1):
        x1 = g(x0)
        print(i, "\t\t", format(x1, ".6f"))
        
        if abs(x1 - x0) < tolerance:
            print("\nRoot is:", format(x1, ".6f"))
            return
        
        x0 = x1
    
    print("Solution did not converge")

# Initial guess
x0 = 2
iteration_method(x0)
