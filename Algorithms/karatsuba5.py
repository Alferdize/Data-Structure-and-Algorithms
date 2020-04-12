import math

def karatsuba(n1,n2):
    if n1 < 10 or n2 < 10:
        return n1 * n2
    
    m = min(len(str(n1)), len(str(n2)))
    m1 = m //2
    high1 = n1 // 10**(m1)
    low1 = n1 % 10**(m1)
    high2 = n2 // 10 **(m1)
    low2 = n2 % 10 ** (m1)

    z0 = karatsuba(low1,low2)
    z1 = karatsuba((low1+high1), (low2+high2))
    z2 = karatsuba(high1, high2)

    return (z2 * 10 ** (m1 * 2)) + ((z1 - z2 - z0) * 10 ** m1) + z0




num1 = 3141592653589793238462643383279502884197169399375105820974944592
num2 = 2718281828459045235360287471352662497757247093699959574966967627

print(karatsuba(num1, num2))