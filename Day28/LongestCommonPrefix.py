class Solution:
    def longestCommonPrefix(self, strs) -> str:
        res=0
        for x in range(len(strs[0])):
            word = strs[0][x]
            notmatch = False
            for y in range(1,len(strs)):
                if x>=len(strs[y]) or word!=strs[y][x]:
                    notmatch=True
                    break
                
            if notmatch:
                return strs[0][:res]
            res+=1
        return strs[0][:res]
        
        