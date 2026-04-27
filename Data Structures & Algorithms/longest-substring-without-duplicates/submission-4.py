class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, length = 0, 0
        current = set()

        for r in range(len(s)):
            while s[r] in current:
                current.remove(s[l])
                l += 1
            current.add(s[r])
            length = max(length, r - l + 1)
        

        return length
