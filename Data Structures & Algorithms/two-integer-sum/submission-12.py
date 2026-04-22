class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i, n in enumerate(nums):
            d = target - n
            if d in a:
                return [a[d], i]
            a[n] = i
        
        

