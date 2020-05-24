import re
T = int(input())
for _ in range(T) :
    n = int(input())
    s = input()
    print(len(re.findall(r'([^aeiou])([aeiou])',s)))