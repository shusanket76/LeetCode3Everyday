class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l = 0 
        r = len(tokens)-1
        res = 0
        temp = 0
        while l<=r:
            if tokens[l]<=power:
                temp+=1
                res = max(res, temp)
                power-=tokens[l]
                l+=1
            elif temp>0:
                power+=tokens[r]
                r-=1
                temp-=1
            else:
                return res
        return res