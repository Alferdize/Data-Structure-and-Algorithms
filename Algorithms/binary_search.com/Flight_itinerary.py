class Solution:
    def solve(self, s):
        forward = {k:v for k,v in s}
        back = {v:k for k,v in s}
        b = s[0][1]
        while (nb:=back.get(b)):
            b = nb
        ret = [b]
        f = b
        while (nf:=forward.get(f)):
            ret.append(nf)
            f = nf
        return ret