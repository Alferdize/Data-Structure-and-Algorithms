import re

N = int(input())

string = []
for i in range(N):
    A = input()
    # A = re.sub(r'[^.?"',-;()/[]{}:!]', '', A)
    A = re.sub(r"['.;:]",'',A)
    B = list(map(str,A.split(" ")))
    B.remove("")
    string.append(B)



for i in range(N-1,-1,-1):
    print(" ".join(string[i][::-1]))