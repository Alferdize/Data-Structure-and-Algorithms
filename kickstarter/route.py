case= int(input())

for i in range(case):
    # j,k = 0,0
    string1 = ""
    N = int(input())
    a = [[0]*N]*N
    string = input()
    for l in range(len(string)):
        if string[l] == "S":
            string1 += "E"
        else:
            string1 += "S"
    print("Case #{}: {}".format(i+1,string1))
