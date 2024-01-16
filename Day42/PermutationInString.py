class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s2leftpointer = 0
        s2rightpointer = 0
        s1leftpointer = 0
        hasmap={}
        
        while s1leftpointer<len(s1):
            hasmap[s1[s1leftpointer]]=hasmap.get(s1[s1leftpointer], 0)+1
            s1leftpointer+=1
        def anagram(a1,a2):
            hasmap2 = hasmap.copy()
            l=0
       
            while l<len(a1) and a2[l] in hasmap2:
                hasmap2[a2[l]]-=1
                l+=1
            return min(hasmap2.values())==max(hasmap2.values())==0
        
        while s2rightpointer<len(s2):
            if s2[s2rightpointer] in hasmap and s2rightpointer+len(s1)<=len(s2):
                if anagram(s1, s2[s2rightpointer:s2rightpointer+len(s1)]) is True:
                    return True
            s2rightpointer+=1
        return False

        