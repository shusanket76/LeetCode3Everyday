class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(curr, pointer):
            if len(curr)==k:
                res.append(curr[:])
                return
            if pointer>n:
                return 
            curr.append(pointer)
            dfs(curr, pointer+1)
            curr.pop()
            dfs(curr, pointer+1)
        dfs(curr=[], pointer=1)
        return res