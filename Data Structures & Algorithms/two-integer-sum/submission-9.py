class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        oldMap = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in oldMap:
                return [oldMap[difference], i]
            oldMap[n] = i
        
        

