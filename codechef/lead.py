P1 = 0
P2 = 0

def testcase():
    T = int(input())
    W = 0
    L = 0 
    for i in range(T):
        Win,Lead = Score()
        if Lead > L:
            W = Win
            L = Lead
    print("{} {}".format(W,L))


def Score():
    global P1, P2
    p1,p2 = list(map(int,input().split()))
    P1+=p1
    P2+=p2
    lead = P1 - P2
    if lead > 0:
        return 1, lead
    else:
        return 2, abs(lead)



if __name__ == "__main__":
    testcase()