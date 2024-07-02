class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # le = len(gas)
        # for x in range(len(gas)):
        #     start = x
        #     if gas[start]<cost[start]:
        #         continue
        #     else:
        #         tg = 0
        #         visit = set()
        #         s1 = start
        #         while start<len(gas):
        #             visit.add(start)
        #             tg+=gas[start]
        #             tg-=cost[start]
        #             if tg<0:
        #                 break
        #             start+=1
        #             start = start%le
        #             if start in visit:
        #                 return s1
        # return -1
                
        nums = [gas[x]-cost[x] for x in range(len(gas))]
        total = 0
        for x in nums:
            total+=x
        if total<0:
            return -1
        print(nums)
        start = 0
        curr = 0
        for x in range(len(nums)):
            curr+=nums[x]
            if curr<0:
                
                start=x+1
                curr = 0
        return start%len(nums)