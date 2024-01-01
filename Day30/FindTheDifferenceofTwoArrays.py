class Solution:
    def findDifference(self, nums1, nums2):
        nums1set = set(nums1)
        nums2set = set(nums2)
        arr1 = []
        for x in nums1set:
            if x not in nums2set:
                arr1.append(x)
        arr2 = []
        for y in nums2set:
            if y not in nums1set:
                arr2.append(y)
        return [arr1, arr2]
        