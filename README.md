# Numerical-Analysis



**Bisection Method**
---------------------------------
The bisection method is a technique for finding solutions to equations with a single unknown variable. The bisection method is based on the Intermediate Value Theorem, which states that if f(x) is a continuous function on the interval [a, b] and f(a) and f(b) have opposite signs (i.e., f(a)⋅f(b)<0), then there is at least one root of the equation f(x)=0 in the interval (a,b).


**Assumptions**
1. f(x) is a continuous function on the interval [a, b].
2. f(a)⋅f(b) < 0 ( i.e., the function values at a and b have opposite signs).


**Steps**

1. Find the middle point c = (a + b) / 2

2. If f(c) = 0, then c is the root of the equation.
   
3. If f(c) ≠ 0:
   * If f(a)⋅f(c)<0, the root lies between a and c, so we recur with the interval [ a, c].
     
   *  Else, if f(b)⋅f(c)<0, the root lies between b and ccc, so we recur with the interval [ c, b].
  
4. If neither of these conditions hold, then the function does not satisfy the assumptions of the bisection method.

5. Since the root may be a floating-point number, we repeat the above steps until the difference between a and b is less than or equal to a very small value.



**Falsi Position or Rugla Falsi Method**
----------------------------------------------------------
Regula Falsi Method, also known as the False Position Method, is a numerical method used to find the root of a non-linear equation f(x)=0 by repeatedly narrowing the interval where the sign of the function changes.
* It selects two initial points x₀ and x₁ with opposite signs of f(x), ensuring a root lies between them.

* It works on the principle that a continuous function crossing zero in an interval has a root there.

* Its convergence is faster than the Bisection Method but slower than the Newton-Raphson Method.



**Formula**

The Regula Falsi method uses the following formula to approximate the root:

c = a - ( f(a) * (b - a) ) / f(a) - f(b)

**Where,**
   * a and b are the endpoints of the interval [a, b].
     
   * f(a) and f(b) are the function values at points a and b.
     
   * c is the point where the linear interpolation intersects the x-axis.


**Steps**

  1. Choose two initial points a and b such that function at those points have opposite sign i.e., f(a)⋅f(b) < 0.

  2. Calculate the point c where the linear approximation intersects the x-axis using the formula.

  3. Determine f(c).
      * If f(c) ⋅ f(a) < 0, then the root lies between a and c. Set b = c.
    
      * If f(c) ⋅ f(b) < 0, then the root lies between b and c. Set a = c.
    
   4. Repeat the steps until ∣f(c)∣ is less than a predefined tolerance level or the interval [a, b] is sufficiently small.



**Fixed Point Iteration Method**
--------------------------------------------
The fixed point iteration is a numerical method to approximate solutions of algebraic or transcendental equations by repeatedly applying a function g(x) such that g(x) = x. It simplifies solving complex equations like cubic or transcendental ones. The method finds the root by iterating until successive values converge to a fixed point.


**Steps**

  1. Choose the initial guess x₀ as the average of a and b where f(a) < 0 and f(b) > 0.

  2. Rewrite the equation as x = g(x) with |g’(x₀)| < 1, choosing the g(x) that gives the smallest |g’(x₀)| if multiple forms exist.

  3. Using xn = g(xn–1), the sequence {xn} converges to a fixed point l₀, giving the approximate solution.



**Gaussian Elimination Method**
---------------------------------------------------
The Gaussian Elimination Method is a standard technique for solving systems of linear equations by systematically reducing them to find the values of unknown variables. It has practical applications in areas like traffic flow analysis, where it helps model and optimize the movement of vehicles at intersections, improving efficiency and reducing congestion.


**Steps**

  1. Get a 1 in the first column, first row.
     
  2. Use the 1 to get 0’s in the remainder of the first column.
     
  3. Get a 1 in the second column, second row.
     
  4. Use the 1 to get 0’s in the remainder of the second column.
     
  5. Get a 1 in the third column, third row.



**Gauss Jordan Method**
--------------------------------------------
 The Gauss-Jordan method, also known as Gauss-Jordan elimination method is used to solve a system of linear equations and is a modified version of Gauss Elimination Method. This method is widely used in engineering, mathematics, and computer applications for solving multiple linear equations efficiently.
 

**Steps**

  1. Write the augmented matrix of the system of linear equations.

  2. Transform the pivot element to 1.

  3. Make all other elements in the pivot column zero.

  4. Move to the next pivot.

  5. Read the solution directly.

  6. Check the solution.

     

**Iteration Method**
------------------------------------------
The Iteration Method is a numerical technique used to find approximate solutions of equations, especially when exact solutions are difficult to obtain. It generates a sequence of approximations that converge to the actual solution through repeated application of a formula.


**Steps**

  1. Rewrite the equation in the form x = g(x)

  2. Choose an initial guess x0, preferably close to the root.

  3. Compute the next approximation using the iteration formula:
      x1 = g(x0), x2 = g(x1), x3 = g(x2),........

  4. Check for convergence: If |xn - xn -1| < tolerance, stop the iteration.

  5. Repeat the iteration until the desired accuracy is achieved.

  6. Take the final value as the approximate root of the equation.



**LU Decomposition**
-------------------------------------------
LU decomposition or factorization of a matrix is the factorization of a given square matrix into two triangular matrices, one upper triangular matrix and one lower triangular matrix. It is a fundamental technique in linear algebra used to solve systems of linear equations, invert matrices, and compute determinants. Computers usually solve square systems of linear equations using LU decomposition.

LU Decomposition breaks a square matrix A into two matrices:
L is a lower triangular matrix with 1s on its diagonal, and
U an upper triangular matrix.

So the original matrix can be represented as:

               **A = L × U**
               

**Steps**

 1. Write matrix 𝐴 and initialize L (lower triangular with 1s) and U (upper triangular).

 2. Decompose A into L and U using:
 3. 
     * Uij = Aij - ∑ Lij Ukj(for i <= j)
   
     * Lij = (Aij - ∑ Lik​ Ukj) / Uij(for i > j)

 4. Solve L⋅Y=B (forward substitution) and U⋅X=Y (backward substitution) to get the solution.



**Newton Rapson Method**
----------------------------------------
The Newton-Raphson Method is a numerical technique used to find approximate roots of a real-valued function **f(x)=0**. It is an iterative method that uses the derivative of the function to quickly converge to the root.

**Formula**

The Newton-Raphson method formula is written as follows:

               Xn = Xn - 1 - (f(xn -1) / f′(Xn - 1)

Where, 

  * xn-1 is the estimated (n-1)th root of the function.
    
  * f(xn-1) is the value of the equation at (n-1)th estimated root.
    
  * f'(xn-1) is the value of the first order derivative of the equation or function at xn-1
 

**Steps**

1. f(x) for different values of x .

2. A tangent is drawn to f(x) at x0. This is the initial value.

3. his tangent will intersect the X- axis at some fixed point (x1, 0) if the first derivative of f(x) is not zero i.e. f'(x0) ≠ 0.

4.  As this method assumes iteration of roots, this x1 is considered to be the next approximation of the root.

5.  Now steps 2 to 4 are repeated until we reach the actual root x.


​​
**Eular's Method**
-----------------------------------------------
Euler’s Method is a simple numerical technique used to find approximate solutions of first-order ordinary differential equations (ODEs) of the form:

                        dy / dx = f(x,y),  y(x0) = y0


**Formula**

               Yn+1 = Yn + h.f(Xn,Yn)
               
   where h = step size


**Steps**

 1. Start with the initial condition (x0, y0)

 2. Choose a step size h.

 3. Compute Yn+1 = Yn + h.f(Xn,Yn)

 4. Update Xn+1 = Xn + h and repeat until the desired X is reached.




**Muller's Method**
----------------------------------------------
Muller’s Method is a numerical technique used to find the roots of a non-linear equation f(x)=0. It uses three initial approximations and fits a quadratic curve through them to estimate the root.


**Steps**

1. Choose three initial approximations x0, x1, x2 close to the root.

2. Evaluate the function values f(x0), f(x1), f(x2).

3. Fit a quadratic polynomial through the three points.

4. Compute the root of the quadratic equation to obtain the next approximation x3.

5. Replace the oldest value with x3 and repeat the process.

6. Stop the iteration when the difference between successive approximations is within the desired tolerance.




**Newton Forward And Backward Interpolation**
-----------------------------------------------------------
Newton Forward and Backward Interpolation are numerical techniques used to estimate the value of a function at a point based on known discrete data points. They are commonly used in interpolation, where we want to find values inside the range of given data.


**Steps**

1. Prepare the difference table (forward or backward).

2. Compute u based on the position of the value.

3. Multiply differences with successive u-terms and divide by factorials.

4. Add all terms to the initial value to get the approximate result.
