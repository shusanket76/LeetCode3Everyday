class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        l1 = 0 
        r1 = len(matrix)-1
        while l1<=r1:
            mid = (l1+r1)//2
            if (matrix[mid][0]<target and target<matrix[mid][-1]):
                break
            elif matrix[mid][0]>target:
                r1=mid-1
            elif target>matrix[mid][-1]:
                l1=mid+1
            else:
                break
        
        l2 = 0
        arr = matrix[mid]
        r2 = len(arr)-1
        while l2<=r2:
            mid = (l2+r2)//2
            if arr[mid]==target:
                return True
            elif arr[mid]>target:
                r2=mid-1
            else:
                l2=mid+1
        return False

        