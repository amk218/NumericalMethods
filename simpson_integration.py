"""
Numerical methods examples

Integration with Simpson's rule, using an iterative approach
The algorithm uses the trapezoidal rule to calculate an initial estimate, and then uses two successive iterations
of the trapezoidal rule to calculate an improved estimate

Anni Kauniskangas
2.1.2021
"""

def simpsons_rule(f,a,b,cc):
    h = (b-a)/2
    T_new = 1/2 * h * (f(a)+f(b))  # First estimate
    T_old = 2 * T_new
    S_new = T_new
    S_old = T_old
    j = 1

    while abs((S_new - S_old)/S_old) > cc:  # Run until convergence criterion is met
        print(S_new)
        S_old = S_new
        T_old = T_new
        f_sum = 0
        for i in range(1,int(2**(j-1))):  # Iterate using the trapezoidal rule
            f_sum += f(a + (2*i - 1)*h)
        T_new = 1/2 * T_old + h * f_sum
        S_new = 4/3 * T_new - 1/3 * T_old  # Adjust weighting of two consecutive iterations to get Simpson's rule
        h = h/2
        j += 1

    print("The value of the integral is "+str(S_new))
    return S_new


# Testing
def f(x): # Test function
    return 1
a = 1
b = 2
epsilon = 0.0001
simpsons_rule(f,a,b,epsilon)