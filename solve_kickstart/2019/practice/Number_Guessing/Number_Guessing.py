import sys
T = int(input())
for i in range(T):
    A, B = list(map(int,input().split()))
    N = int(input())
    while True:
        guess = (A + B + 1) //2
        print(guess)
        sys.stdout.flush()
        msg = input()
        if msg == "TOO_BIG":
            B = guess - 1
        elif msg == "TOO_SMALL":
            A = guess
        elif msg == "CORRECT":
            break
        else:
            sys.stderr.write("Error")