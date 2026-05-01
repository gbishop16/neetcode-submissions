class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        data = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in data:
                return [data[diff], i]
            data[n] = i
        
            
