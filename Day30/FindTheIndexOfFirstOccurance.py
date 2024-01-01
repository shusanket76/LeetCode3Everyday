class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nl = 0
        nr = 0
        hl = 0
        hr = 0
        res = float("inf")
        while hr<len(haystack):
            if needle[nr]==haystack[hr]:
                nr+=1
                hr+=1
            else:
                nr = 0
                hr = hl
                hl+=1

            if nr==len(needle):
                res=min(res,hr-len(needle))
                nr = 0
        if res==float("inf"):
            return -1
        return res