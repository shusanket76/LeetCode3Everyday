class Solution:
    def totalFruit(self, fruits) -> int:
        hasmap = {}
        leftpointer = 0
        rightpointer = 0
        difftype = 0
        ans = 0
        while rightpointer<len(fruits):
            if fruits[rightpointer] not in hasmap:
                difftype+=1
                hasmap[fruits[rightpointer]]=1
                while difftype>2:
                    hasmap[fruits[leftpointer]]-=1
                    if hasmap[fruits[leftpointer]]==0:
                        difftype-=1
                        hasmap.pop(fruits[leftpointer])
                    leftpointer+=1
            
            else:
                hasmap[fruits[rightpointer]]+=1
            ans = max(ans, rightpointer-leftpointer+1)
            rightpointer+=1
        return ans

        