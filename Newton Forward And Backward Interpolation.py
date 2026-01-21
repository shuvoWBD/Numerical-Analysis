# Python3 Program for Newton Forward & Backward Interpolation

# Function to calculate u for forward interpolation
def u_cal_forward(u, n):
    temp = u
    for i in range(1, n):
        temp *= (u - i)
    return temp

# Function to calculate u for backward interpolation
def u_cal_backward(u, n):
    temp = u
    for i in range(1, n):
        temp *= (u + i)
    return temp

# Factorial function
def fact(n):
    f = 1
    for i in range(2, n+1):
        f *= i
    return f

# Newton Forward Interpolation
def newton_forward(x, y_values, value):
    n = len(x)
    # Create forward difference table
    y = [[0 for _ in range(n)] for __ in range(n)]
    for i in range(n):
        y[i][0] = y_values[i]

    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = y[j+1][i-1] - y[j][i-1]

    u = (value - x[0]) / (x[1] - x[0])
    sum_val = y[0][0]

    for i in range(1, n):
        sum_val += (u_cal_forward(u, i) * y[0][i]) / fact(i)

    return round(sum_val, 6)

# Newton Backward Interpolation
def newton_backward(x, y_values, value):
    n = len(x)
    # Create backward difference table
    y = [[0 for _ in range(n)] for __ in range(n)]
    for i in range(n):
        y[i][0] = y_values[i]

    for i in range(1, n):
        for j in range(n-1, i-1, -1):
            y[j][i] = y[j][i-1] - y[j-1][i-1]

    u = (value - x[-1]) / (x[1] - x[0])
    sum_val = y[n-1][0]

    for i in range(1, n):
        sum_val += (u_cal_backward(u, i) * y[n-1][i]) / fact(i)

    return round(sum_val, 6)

# -------------------- Example Usage --------------------

# Forward Example
x_forward = [45, 50, 55, 60]
y_forward = [0.7071, 0.7660, 0.8192, 0.8660]
value_forward = 52

result_forward = newton_forward(x_forward, y_forward, value_forward)
print("Newton Forward Interpolation: Value at", value_forward, "is", result_forward)

# Backward Example
x_backward = [1891, 1901, 1911, 1921, 1931]
y_backward = [46, 66, 81, 93, 101]
value_backward = 1925

result_backward = newton_backward(x_backward, y_backward, value_backward)
print("Newton Backward Interpolation: Value at", value_backward, "is", result_backward)
