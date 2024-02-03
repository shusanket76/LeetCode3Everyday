def numSubseq(nums, target: int) -> int:
        nums.sort()
        res = [0]


        def dfs(curr, pointer):
            if pointer>=len(nums) and len(curr)!=0:
                if curr[0]+curr[-1]<=target:
                    res[0]+=1
                return 
            if pointer>=len(nums):
                return
            curr.append(nums[pointer])
            dfs(curr, pointer+1)
            curr.pop()
            dfs(curr, pointer+1)

        
        curr = []
        pointer = 0
        dfs(curr, pointer)
        print(res)
nums = [2,3,3,4,6,7]
target = 12
a = numSubseq(nums, target)        