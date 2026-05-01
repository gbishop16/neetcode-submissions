class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #return sorted(s) == sorted(t)

        freqS, freqT = {}, {}

        if len(s) != len(t):
            return False

        for i in s:
            freqS[i] = freqS.get(i, 0) + 1

        for i in t:
            freqT[i] = freqT.get(i, 0) + 1
        
        for key in freqS:
            if freqS[key] != freqT.get(key, 0):
                return False
        
        return True
        
        
