class Solution:
    def numUniqueEmails(self, emails) -> int:
        res = set()
        for x in emails:
            l=0
            r=len(x)-1
            newemail = ""
            while l<=r:
                if x[l]==".":
                    l+=1
                elif x[l]=="+":
                    while x[l]!="@":
                        l+=1
                elif x[l]=="@":
                    while l<=r:
                        newemail+=x[l]
                        l+=1
                else:
                    newemail+=x[l]
                    l+=1
            res.add(newemail)
        return len(res)

        