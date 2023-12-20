class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        haset = set()
        first = 0
        second = 0
        res = 0
        while second<len(s):
            if s[second] not in haset:
                haset.add(s[second])
                res = max(res, second-first+1)
                second+=1
            else:
                while s[second] in haset:
                    haset.remove(s[first])
                    first+=1
            

        return res