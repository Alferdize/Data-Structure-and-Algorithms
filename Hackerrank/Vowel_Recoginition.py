from sys import stdout,stdin
 
def main():
    t=int(stdin.readline())
    while(t):
        string=stdin.readline().strip()
        l=len(string)
        total=0
        for i in range(l):
            if string[i] in 'aeiouAEIOU':
                total+=(i+1)*(l-i)
        stdout.write(str(total)+'\n')
       
        t-=1
        
if __name__ =='__main__':
    main()