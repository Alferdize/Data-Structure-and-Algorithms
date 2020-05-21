n= int(input())
for i in range(n):
    a=list(input())
    b=list(input())
    s=set(a+b)
    c=0
    for i in s:
        c=c+min(a.count(i),b.count(i))
    print(len(a)+len(b)-2*c)