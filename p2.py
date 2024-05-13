def subsets(nums):
        res = []
        def dfs(curr, pointer):
            if pointer==len(nums):
                res.append(curr[:])
                return 
            if pointer>len(nums):
                return 
            curr.append(nums[pointer])
            dfs(curr, pointer+1)
            curr.pop()
            dfs(curr, pointer+1)            
        curr = []
        pointer = 0
        dfs(curr, pointer)
        return res
    
a = subsets([1,2,3])