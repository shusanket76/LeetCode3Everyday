class Solution:
    def topKFrequent(self, nums, k: int):
        count = [[] for x in range(len(nums)+1)]
        hasmap = {}
        res = []
        for x in nums:
            hasmap[x] = hasmap.get(x,0)+1
        for a,b in hasmap.items():
            count[b].append(a)
    
    
        for y in range(len(count)-1,-1,-1):
            if len(count[y])!=0:
                
                for d in count[y]:
                  
                    res.append(d)
                    if len(res)==k:
                        return res
        