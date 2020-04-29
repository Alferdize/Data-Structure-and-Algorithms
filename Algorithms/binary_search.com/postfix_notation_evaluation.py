import operator as op
class Solution:
    def solve(self,exp):
        ops = {"*":op.mul, "+":op.add,"-":op.sub,"/":lambda x,y: int(op.truediv(x,y))}
        stack = []
        for c in exp:
            if c not in ops:
                stack.append(int(c))
            else:
                right = stack.pop()
                left = stack.pop()
                stack.append(ops[c](left,right))
        return stack.pop()