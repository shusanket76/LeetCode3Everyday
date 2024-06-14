def totalMoney(n: int) -> int:
        l = 0
        r = 1
        s = 0
        while l<n:
            if l+7>n:
                s+=(r+(l+6-n))*(n-r+1)//2
                l+=(n-r+1)
            else:
                s+=(r+6+r)*(7)//2
                l+=7
            r=r+1
        return s
a=totalMoney(10)