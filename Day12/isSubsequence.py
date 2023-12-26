class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a = 0
        b = 0
        while a<=len(t):
            if b==len(s):
                return True
            if a==len(t):
                return False
            elif t[a]==s[b]:
                b+=1
                a+=1
            else:
                a+=1
   
        return False
        