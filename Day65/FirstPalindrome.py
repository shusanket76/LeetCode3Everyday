class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def ispalindrome(x):
            l=0
            r = len(x)-1
            while l<=r:
                if x[l]!=x[r]:
                    return False
                l+=1
                r-=1
            return True
        for x in words:
            if ispalindrome(x) is True:
                return x
        return ""
        