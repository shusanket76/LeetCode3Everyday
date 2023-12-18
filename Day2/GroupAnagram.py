from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        hasmap = defaultdict(list)
        for x in strs:
            count = [0 for a in range(26)]
            for y in x:
                order = ord(y)-ord("a")
                count[order]+=1
            hasmap[tuple(count)].append(x)
        return hasmap.values()
