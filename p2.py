def largestNumber(nums) -> str:
        for y in range(len(nums)):
            for x in range(len(nums)-1-y):
                a = str(nums[x])+str(nums[x+1])
                b = str(nums[x+1])+str(nums[x])
                if int(a)<int(b):
                    nums[x],nums[x+1]=nums[x+1], nums[x]
        print(nums)


a = largestNumber([3,30,34,5,9])