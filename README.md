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

5. Since the root may be a floating-point number, we repeat the above steps until the difference between a and b is less than or equal to a very small value

