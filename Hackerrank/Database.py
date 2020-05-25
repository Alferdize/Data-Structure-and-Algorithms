import sys
 
for _ in range(int(sys.stdin.readline())):
    cad , rad = map(int, sys.stdin.readline().split())
    d = [list(sys.stdin.readline().split()) for _ in range(rad + 1)]
    w = [max(a) for a in zip(*(list(map(len, b)) for b in d))]
    u = '+' + '+'.join('-' * (x + 2) for x in w) + '+'
    print(u)
    print('| ' + ' | '.join(d[0][i].ljust(w[i]) for i in range(cad)) + ' |')
    print(u)
    for a in d[1:]:
        print('| ' + ' | '.join(
            a[i].rjust(w[i]) if a[i][0] in '0123456789' and '/' not in a[i] else a[i].ljust(w[i]) for i in
            range(cad)) + ' |')
    print(u)