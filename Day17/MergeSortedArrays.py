class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1=0
        l2=0
        res= len(nums1)-len(nums2)

        while l2<len(nums2):
            if nums1[l1]>nums2[l2] or (len(nums2)-l2==len(nums1)-l1):
                nums1.insert(l1, nums2[l2])
                nums1.pop()
                l2+=1
            else:
                l1+=1
