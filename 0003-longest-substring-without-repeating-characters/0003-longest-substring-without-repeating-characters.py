class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        m = []
        strs = ""
        c = 0

        for i in range(len(s)):
            if s[i] not in strs:
                strs += s[i]
                c += 1
            else:
                m.append(c)

                while s[i] in strs:
                    strs = strs[1:]
                    c -= 1

                strs += s[i]
                c += 1

        m.append(c)

        return max(m)