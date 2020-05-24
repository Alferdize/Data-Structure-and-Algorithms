from sys import stdin, stdout
A=0
B=7
for i in range(int(stdin.readline())):
    N=int(stdin.readline())
    if((N-A)<=(B-N)):
        stdout.write("A\n")
        A=N
    else:
        stdout.write("B\n")
        B=N