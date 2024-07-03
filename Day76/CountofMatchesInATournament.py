class Solution:
    def numberOfMatches(self, n: int) -> int:
        totalmatch = 0
        while n!=1:
            if n%2==0:
                totalmatch+= n/2
                n = n/2
            else:
                totalmatch+= (n-1)/2
                n = ((n-1)/2)+1
        return int(totalmatch)

        