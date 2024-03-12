from collections import deque
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        queue = deque()
        for index,val in enumerate(dominoes):
            if val!=".":
                queue.append((index, val))
        while queue:
            index, curr = queue.popleft()
            if curr=="L":
                if index-1>=0 and dominoes[index-1]==".":
                    queue.append((index-1, "L"))
                    dominoes[index-1]='L' 
            elif curr=="R":
                if (index+1)<len(dominoes) and dominoes[index+1]==".":
                    if (index+2)<len(dominoes) and dominoes[index+2]=="L":
                        queue.popleft()
                    else:
                        queue.append((index+1, "R"))
                        dominoes[index+1] = "R"
        res = ""
        for y in dominoes:
            res+=y
        return res