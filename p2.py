def minSubArrayLen(target: int, nums) -> int:
    nums.sort()
    r = 0
    l = 0
    reslen = float("inf")
    wehave = 0
    while r < len(nums):
        wehave += nums[r]
        if wehave >= target:
            if (r - l + 1) < reslen:
                reslen = r - l + 1
            wehave -= nums[l]
            l += 1
        r += 1
    r-=1
    while l<len(nums):
        if wehave>=target:
            if (r - l + 1) < reslen:
                reslen = r - l + 1
        wehave-=nums[l]
        l += 1

        
    if reslen == float("inf"):
        return 0
    return reslen

a = minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
print(a)