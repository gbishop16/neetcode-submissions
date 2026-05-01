class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return sorted(s) == sorted(t)

        # freqS, freqT = {}. {}

        # if len(s) != len(t):
        #     return False
        
