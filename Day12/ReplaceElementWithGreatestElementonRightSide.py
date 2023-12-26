class Solution:
    def replaceElements(self, arr):
        i = len(arr)-2
        maxarr = [-1]
        maxright = -1
        while i>=0:
            maxright = max(arr[i+1], maxright)
            maxarr.insert(0, maxright)
            i-=1
        return maxarr
        