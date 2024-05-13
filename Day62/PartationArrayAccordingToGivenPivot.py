class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        prevelements = []
        nextelements = []
        pivotelements = []
        for x in nums:
            if x<pivot:
                prevelements.append(x)
            elif x>pivot:
                nextelements.append(x)
            else:
                pivotelements.append(x)
        nums = prevelements+pivotelements+nextelements
        return nums