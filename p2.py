def findClosestElements(arr, k: int, x: int):
    # binary search to see whether x is in the array or not
        res = []
        def binarysearch():
            l = 0 
            r = len(arr)-1
          
            while l<=r:
                mid = (l+r)//2
                if arr[mid]==x:
                    res.append(arr[mid])
                    return mid
                elif arr[mid]>x:
                    r=mid-1
                else:
                    l=mid+1
            return mid+1

        startingpos = binarysearch()
        if len(res)==0:
            right = startingpos
        else:
            right = startingpos+1
        left = startingpos-1
        while len(res)<k:
            if left>=0 and right<len(arr):
                if abs(arr[left]-x)==abs(arr[right]-x) and left<right:
                    res.append(arr[left])
                    left-=1
                elif abs(arr[left]-x)<abs(arr[right]-x):
                    res.append(arr[left])
                    left-=1
                else:
                    res.append(arr[right])
                    right+=1
            elif left>=0:
                res.append(arr[left])
                left-=1
            elif right<len(arr):
                res.append(arr[right])
                right+=1
        res.sort()
        return res
        
            
a = findClosestElements([1,5,10], 1, 4)
print(a)
