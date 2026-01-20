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


