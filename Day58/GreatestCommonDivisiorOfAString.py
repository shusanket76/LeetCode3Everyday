class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if len(str1)<len(str2):
            r1 = len(str1)
            smallword = str1
            bigword = str2
        else:
            r1 = len(str2)
            smallword = str2
            bigword = str1
        
        while r1>0:
            if len(smallword)%(r1)==0:
                add = len(smallword)//(r1)
                prefix = smallword[0:r1]*add
                if prefix==smallword:
                    if len(bigword)%(r1)==0:
                        add = (len(bigword)//(r1))
                        prefix = smallword[0:r1]*add
                        if prefix== bigword:
                            return smallword[0:r1]
            r1-=1
        return ""