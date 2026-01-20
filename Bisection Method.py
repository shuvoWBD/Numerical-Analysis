# Python program for implementation of Bisection Method for solving equations
# Example function: x^3 - x^2 + 2

def func(x):
    return x**3 - x**2 + 2


def bisection(a, b):
    if func(a) * func(b) >= 0:
        print("You have not assumed right a and b")
        return

    c = a
    while (b - a) >= 0.01:
        # Find middle point
        c = (a + b) / 2

        # Check if middle point is root
        if func(c) == 0.0:
            break

        # Decide the side to repeat the steps
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c

    print("The value of root is:", format(c, ".4f"))


# Driver code
a = -200
b = 300
bisection(a, b)

