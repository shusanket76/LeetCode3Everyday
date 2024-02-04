# # BRUTE FORCE



# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         res = []
#         for x in nums1:
#             for y in range(len(nums2)):
#                 if x==nums2[y]:
#                     greater = False
#                     for z in range(y+1, len(nums2)):
#                         if nums2[z]>nums2[y]:
#                             res.append(nums2[z])
#                             greater = True
#                             break
                    
#                     if not greater:
#                         res.append(-1)

            
#         return res
            


        

# //OPTIMAL 
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hasmap = {i:x for x,i in enumerate(nums1)}
        
        res = [-1 for y in range(len(nums1))]
        stack = []
        i=0
        while i<len(nums2):
            curr = nums2[i]
            while stack and curr>stack[-1]:
                hid = hasmap[stack[-1]]
                res[hid] = curr
                stack.pop()
            if curr in hasmap:
                stack.append(curr)
            i+=1
        return res
            
    
            


        