class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        r = 0
        res = [0]
        tempres = 0
        haset = set()
        haset.add("a")
        haset.add("e")
        haset.add("i")
        haset.add("o")
        haset.add("u")
        while r<len(s):
            if s[r] in haset:
                tempres+=1
            while ((r-l+1)>=k):
                res[0] = max(res[0], tempres)
                if s[l] in haset:
                    tempres -=1
                l+=1
            r+=1

        return(res[0])

        