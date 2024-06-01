def lengthOfLIS(nums) -> int:
        finalres = [0]
        def dfs(pointer, prev):
            if pointer==len(nums):
                return 0
            if prev>=nums[pointer]:
                return -1
            res = 0
            for y in nums:
                prev = y
                for x in range(pointer+1, len(nums)+1):

                    a = dfs(x, prev)+1
                    if res<a:
                        res = a
            return res
        pointer = 0
        prev = nums[0]-1
        
        return dfs(pointer, prev)
a = lengthOfLIS([10,9,2,5,3,7,101,18])
print(a)