class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = x
        new = 0
        while num>0:
            temp=num%10
            new = new *10 + temp
            
            num=num//10
        return new == x