class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hasmap = {}
        def dfs(s, wordDict):
            if s in hasmap:
                return False
            if len(s)==0:
                return True
            for x in wordDict:
                if s[0:len(x)]==x:
                    a = dfs(s[len(x):], wordDict)
                    if a is True:
                        return True
            hasmap[s]= False
            return False
        return dfs(s, wordDict)

        