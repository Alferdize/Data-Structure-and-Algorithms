cases = int(input())


def solve(Total,j):
    string1 = ""
    string2 = ""
    num = str(Total)
    for i in range(len(num)):
        if num[i] == "4":
            string1 += "3"
            string2 += "1"
        elif string2 != "" and num[i] != "4":
            string1 += num[i]
            string2 += "0"
        else:
            string1 += num[i]
            string2 += ""
    return "Case #{}: {} {}".format(j+1,string1,string2)


for i in range(cases):
    Total = int(input())
    print(solve(Total,i))
        