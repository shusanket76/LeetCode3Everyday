from collections import deque
class Solution:
    def decodeString(self, s: str) -> str:
        digi = "01234567789"
        stacktype = deque()
        stackcounter = deque()
        for x in range(len(s)):
            if s[x] in digi:
                stacktype.append("num")
                stackcounter.append(s[x])
            elif s[x]=="[":
                stacktype.append("op")
                stackcounter.append(x)
            elif s[x]=="]":
                newstr = ""
                while stacktype[-1]!="op":
                    newstr=stackcounter.pop()+newstr
                    stacktype.pop()
                openpointer = stackcounter[-1]
                stackcounter.pop()
                stacktype.pop()
                mul = ""
                while len(stacktype)>0 and stacktype[-1]=="num":
                    mul = stackcounter[-1]+mul
                    stackcounter.pop()
                    stacktype.pop()
                if len(mul)==0:
                    mul=1
                val = int(mul) * str(newstr)
                stackcounter.append(val)
              
                stacktype.append("val")
            else:
                stackcounter.append(s[x])
                stacktype.append("val")
        newstr = ""
        for x in stackcounter:
            newstr+=x
        return newstr

            