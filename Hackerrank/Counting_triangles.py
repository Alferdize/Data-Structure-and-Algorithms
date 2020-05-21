n=int(input())
dict={}
while(n>0):
    a=list((input().split()))
    a.sort()
    a=''.join(a)
    if a in dict:
        dict[a]+=1
    else:
        dict[a]=1
    n-=1
cc=0
for key,value in dict.items():
    if(dict[key]==1):
        cc+=1
print(cc)