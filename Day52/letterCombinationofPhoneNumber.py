class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hasmap = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs","8":"tuv", "9":"wxyz"}

        res =[]
        temp = []
        def dfs(digits, word):
            if len(digits)==0:
                res.append(word)
                return
            
            for y in hasmap[digits[0]]:
                    for z in y:
                        word+=z
                        dfs(digits[1:], word)
                        word=word[:len(word)-1]
        if digits=="":
            return []
        dfs(digits,"")
        return res