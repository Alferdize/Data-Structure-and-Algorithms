def findLongestPalindrome(S):
    if S == None or len(S) == 0:
        return ""
    S2 = addBoundaries(S)
    p = [0] * len(S2)
    c = r = m = n = 0
    for i in range(1, len(S2)):
        if i > r:
            p[i], m, n = 0, i-1, i*1
        else:
            i2 = c * 2 - i
            if p[i2] < (r - i - 1):
                p[i] = p[i2]
                m = -1
            else:
                p[i] = r - i
                n = r + 1
                m = i * 2 - n

        while m >= 0 and n < len(S2) and S2[m] == S2[n]:
            p[i] += 1
            m -= 1
            n += 1
        if ((i + p[i]) > r):
            c, r = i, i + p[i]

    length = c = 0
    for i in range(1, len(S2)):
        if length < p[i]:
            length = p[i]
            c = i

    SS = S2[c - length: c + length + 1]
    return "".join(removeBoundaries(SS))


def addBoundaries(S):
    if S == None or len(S) == 0:
        return "||"
    S2 = [0] * (len(S) * 2 + 1)
    for i in range(0, len(S2) - 1, 2):
        S2[i] = "|"
        S2[i+1] = S2[i//2]

    S2[len(S2) - 1] = "|"
    return S2


def removeBoundaries(S):
    if S == None or len(S) < 3:
        return [""]
    n = (len(S)-1)//2
    s2 = [0] * n
    for i in range(0, len(s2)):
        s2[i] = S[i * 2 + 1]
    return s2


print(findLongestPalindrome("adbs"))
