def main():
    from sys import stdin, stdout
    n,q=map(int,stdin.readline().split())
    a=[0]
    for x in stdin.readline().split():
        a.append(int(x)+a[-1])
    res=""
    for Inp in stdin.readlines():
        l,r=map(int,Inp.split())
        n=r-l+1
        S=a[r]-a[l-1]
        res+=str(S//n)+"\n"
    stdout.write(res)
 
if __name__ == "__main__":
    main()