class Solution:
    def reverseString(self, s: List[str]) -> None:
        l=len(s)
        t=""
        for i in range(l//2):
            t=s[i]
            s[i]=s[l-i-1]
            s[l-i-1]=t




        """
        Do not return anything, modify s in-place instead.
        """
        