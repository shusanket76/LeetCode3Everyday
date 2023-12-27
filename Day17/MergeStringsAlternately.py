class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=0
        l2=0
        newword = ""
        while l2<len(word2) and l1<len(word1):
            newword+=word1[l1]+word2[l2]
            l1+=1
            l2+=1
        if l2<len(word2):
            newword+=word2[l2:]
        else:
            newword+=word1[l1:]

        return newword