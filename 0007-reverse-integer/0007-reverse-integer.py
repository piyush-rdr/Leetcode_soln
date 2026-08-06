class Solution:
    def reverse(self, x: int) -> int:
        rev = 0

        if x < 0:
            m = -x
        else:
            m = x

        while m != 0:
            temp = m % 10
            rev = rev * 10 + temp
            m = m // 10

        if x < 0:
            rev = -rev

        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev