def countSubstrings(s: str) -> int:
        res = []
        def ispermutation(word):
            l = 0
            r = len(word)-1
            while l<=r:
                if word[l]!=word[r]:
                    return False
                l+=1
                r-=1
            return True
        
        def dfs(s, curr):
            for x in range(len(s)):
                if ispermutation(curr+s[:x+1]) is True:

                    res.append(curr+s[:x+1])
                    dfs(s[x+1:], curr+s[:x+1]) 
        dfs(s, curr="")
        print(res)
        return len(res)
a = countSubstrings("aaa")
        