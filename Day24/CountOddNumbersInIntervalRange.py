class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count=0
        total = (high-low+1)
        if total%2==0:
            return total//2
        else:
            if low%2!=0:
                return (total//2) +1
            else:
                a=(int)(total//2)
                return a