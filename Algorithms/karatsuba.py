import math
def karatsuba(num1,num2):
    if (num1 < 10) or (num2 < 10):
        return num1 * num2
    m = min(len(str(num1)), len(str(num2)))
    m2 = math.floor(m // 2)
    a = num1 // 10**(m2)
    b = num1 % 10**(m2)
    c = num2 // 10**(m2)
    d = num2 % 10**(m2)
    z0 = karatsuba(b, d)
    z1 = karatsuba((a + b), (c + d))
    z2 = karatsuba(a, c)
    return (z2 * 10 ** (m2 * 2)) + ((z1 - z2 - z0) * 10 ** m2) + z0
    


num1 = 3141592653589793238462643383279502884197169399375105820974944592
num2 = 2718281828459045235360287471352662497757247093699959574966967627

print(karatsuba(num1,num2))