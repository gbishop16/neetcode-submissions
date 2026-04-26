class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        sLow = s.lower()

        while i < j:
            while i < len(sLow) and not sLow[i].isalnum():
                i += 1
            while j >= 0 and not sLow[j].isalnum():
                j -= 1
            if i > j:
                break
            if sLow[i] != sLow[j]:
                return False

            i += 1
            j -= 1

        return True
