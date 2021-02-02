"""
Numerical methods examples
Integration with the trapezoidal rule, using an iterative approach

Anni Kauniskangas
2.1.2021
"""

def trapezoidal_rule(f,a,b,cc):
    h = (b-a)/2
    I_new = 1/2 * h * (f(a)+f(b))  # First estimate
    I_old = 2 * I_new
    j = 1

    while abs((I_new - I_old)/I_old) > cc:
        I_old = I_new
        f_sum = 0
        for i in range(1,int(2**(j-1))):
            f_sum += f(a + (2*i - 1)*h)

        I_new = 1/2 * I_old + h * f_sum
        h = h/2
        j += 1

    print("The value of the integral is "+str(I_new))
    return I_new


# Testing

def f(x): # Test function
    return x

a = 1
b = 2
epsilon = 0.0001
trapezoidal_rule(f,a,b,epsilon)







