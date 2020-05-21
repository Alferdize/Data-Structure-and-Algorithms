x = [-11, 11, 9, 7, 5, 3, 1, -1, -3, -5, -7, -9 ]
y = ['WS', 'WS', 'MS', 'AS', 'AS', 'MS' ]
# Write your code here
T = int(input())
for i in range(T):
    num = int(input())
    print((' '.join([str(num+x[num%12]), y[num%6]])))