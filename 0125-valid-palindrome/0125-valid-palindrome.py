class Solution:
    def isPalindrome(self, s: str) -> bool:
       
        l = ""
        r = ""
        
        for i in range(len(s)):
            if s[i].isalnum():
                l += s[i].lower()

        for i in range(len(s) - 1, -1, -1):
            if s[i].isalnum():
                r += s[i].lower()

        if l == r:
            return True
        else:
            return False