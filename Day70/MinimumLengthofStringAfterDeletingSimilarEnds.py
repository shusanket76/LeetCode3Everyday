class Solution:
    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s)-1
        while l<r:
            al = 0
            while l<r and s[l]==s[l+1]:
                al+=1
                l+=1
            ar = 0
            while l<r and s[r]==s[r-1]:
                ar+=1
                r-=1
            if s[l]==s[r]:
                l=l+1
                r=r-1
            else:
                print(s[l-al:r+1+ar])
      
                return len(s[l-al:r+1+ar])
        if l==r:
            return 1
        return 0