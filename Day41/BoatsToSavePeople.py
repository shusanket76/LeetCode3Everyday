class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        print(people)
        l=0
        r = len(people)-1
        res=0
        while l<=r:
            if l==r:
                res+=1
                l+=1

            elif people[l]+people[r]<=limit:
                l+=1
                r-=1
                res+=1
            else:
                res+=1
                r-=1

            
        return res

        