def subarraySum(nums, k: int) -> int:
        res = 0
        for x in range(len(nums)):
            temp = nums[x]
            if temp==k:
                res+=1
                continue
            for y in range(x+1, len(nums)):
                temp+=nums[y]
                if temp>k:
                    break
                if temp==k:
                    res+=1
        return res

a  = subarraySum([1,2,3],3)
print(a)