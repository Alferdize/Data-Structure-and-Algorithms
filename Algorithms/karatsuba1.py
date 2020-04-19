def karat(n1,n2):
    if n1 < 10 or n2 < 10:
        return n1 * n2
    m = min(len(str(n1)), len(str(n2)))
    m1 = m // 2

    a = n1 // 10 ** (m1)
    b = n1 % 10 ** (m1)
    c = n2 // 10 ** (m1)
    d = n2 % 10 ** (m1)

    z0 = karat(b,d)
    z1 = karat((a+b),(c+d))
    z2 = karat(a,c)

    return (z2 * 10 ** (m1 * 2)) + ((z1 - z2 -z0) * 10 ** m1) + z0


num1 = 3141592653589793238462643383279502884197169399375105820974944592
num2 = 2718281828459045235360287471352662497757247093699959574966967627

print(karat(num1, num2))