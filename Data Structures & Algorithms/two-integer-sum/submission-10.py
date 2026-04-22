class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in a:
                return [a[difference], i]
            a[n] = i
        
        

