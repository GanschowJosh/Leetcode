"""
 Repeatedly squaring the base x if n is even, 
 and reducing n by 1 if n is odd, until n becomes 0. 
 If n is negative, it calculates the reciprocal of x and
 changes n to positive. 
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return self.myPow(1/x, -n)
        elif n % 2:
            return x * self.myPow(x, n-1)
        else:
            return self.myPow(x*x, n/2)
