def longestPalindrome( s: str) -> str:
        mid = 0
        res = ["",float("-inf")]
        l = mid+1
        r = mid-1

        while mid<len(s):
            l = mid-1
            r = mid+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
                if res[1]<(r-l+1):
                    res[0]=s[l:r+1]
                    res[1] = r-l+1
            mid+=1
        mid1=0
        mid2=1
        l = mid1+1
        r = mid2-1
        while mid2<len(s):
            l = mid1-1
            r = mid2+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
                if res[1]<(r-l+1):
                    res[0]=s[l:r+1]
                    res[1] = r-l+1
            mid1+=1
            mid2+=1
        print(res[0])
        return res[0]
            

a = longestPalindrome("babad")

        