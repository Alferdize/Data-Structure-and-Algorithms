# T = int(input())
# for i in range(T):
#     A = list(input())
#     A = list(map(int,A))
#     last = 0
#     res = ""
#     for j in range(len(A)):
#         res += "("*(A[j] - last)
#         res += ")" * (last - A[j])
#         res += str(A[j])
#         if j == len(A)-1:
#             if last > A[j]:
#                 res += ")" * (last - A[j])
#             else:
#                 res += ")" * (A[j])
#         last = A[j]
#     print("Case #{}: {}".format(i+1,res))

T = int(input())
for i in range(1, T+1):
    A = input()
    res = ""
    last = 0
    for j in range(len(A)):
        if last < int(A[j]):
            res +="(" * (int(A[j]) - last)
            res += A[j]
            last = int(A[j])
        else:
            res +=")" * (last - int(A[j]))
            res += A[j]
            last = int(A[j])
        if j == len(A)-1:
            res += ")" * (last)
    print("Case #{}: {}".format(i,res))
    