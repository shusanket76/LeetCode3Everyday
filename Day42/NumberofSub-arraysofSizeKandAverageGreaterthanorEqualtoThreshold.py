class Solution:
    def numOfSubarrays(self, arr, k: int, threshold: int) -> int:
        l= 0 
        r =0
        res = 0
        total= 0
        while r<len(arr):
            total+=arr[r]
            if (r-l+1)==k:
                if total//k>=threshold:
                    res+=1
                total-=arr[l]
                l+=1
            r+=1
        return res