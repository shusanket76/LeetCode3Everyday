from collections import deque
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = deque()
        l = 0
        r = 0
        while r<len(path):
            while r<len(path) and path[r]!="/":
                r+=1
      
            if l==r:
                if len(stack)==0:
                    
                    stack.append(path[l:r+1])
                l=r+1
                
            elif path[l:r+1]=="./":
                l=r+1
                

            elif path[l:r+1]=="../":
                l=r+1
                if len(stack)>1:
                    stack.pop()
            else:
                if path[l:r+1]=="..":
                    if len(stack)>1:
                        stack.pop()
                elif path[l:r+1]==".":
                    pass
                else:
                    stack.append(path[l:r+1])
                l=r+1
            r+=1
        if l<r:
            if path[l:r+1]=="..":
                stack.pop()
        newpath = ""
        for x in stack:
            newpath+=x

        if len(newpath)>1 and newpath[-1]=="/":
            return newpath[0:-1]
        
        return newpath