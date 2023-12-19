class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        character = "abcdefghijklmnopqrstuvwxyz0123456789"
        right = len(s)-1
        while left<=right:
            while left<=right and  s[left].lower() not in character:
                left+=1
            while left<=right and  s[right].lower() not in character:
                right-=1
            if left<=right and s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
        return True
        