class Solution:
    def numDecodings(self, s: str) -> int:
        hasmap = {}

        def dfs(pointer, curr):

            if (len(curr)!=0 and int(curr)<=26) and pointer in hasmap:
                return hasmap[pointer]
            
            if pointer==len(s) and curr[0]!="0" and int(curr)<=26:
                return 1
            if pointer>len(s) or (len(curr)!=0 and curr[0]=="0" ) or (len(curr)!=0 and int(curr)>26) :
                return 0
                
            
            hasmap[pointer] =  dfs(pointer+1, s[pointer:pointer+1]) + dfs(pointer+2, s[pointer:pointer+2])
            return hasmap[pointer]
        
        pointer = 0
        curr = ""
        return dfs(pointer, curr)
        