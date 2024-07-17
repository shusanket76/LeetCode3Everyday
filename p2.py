from collections import deque
def find132pattern(nums) -> bool:
        stack = deque()
        minval = float("inf")
        x = 0
        while x<len(nums):
            if len(stack)==0:
                stack.append(nums[x])
            else:
                if stack[-1]<=nums[x]:
                    while len(stack)!=0 and stack[-1]<=nums[x]:
                        minval = min(minval, stack[-1])
                        stack.pop()
                    if len(stack)!=0 and nums[x]>minval:
                        return True
                    stack.append(nums[x])
                else:
                    if nums[x]>minval:
                        return True
                    stack.append(nums[x])
            
            x+=1
        return False
a  = find132pattern([1,0,1,-4,-3])
print(a)