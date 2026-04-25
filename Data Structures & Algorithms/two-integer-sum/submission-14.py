class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        store = {} # val : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in store:
                return [store[diff], i]
            store[n] = i



#        for i in range(len(nums)):
#            diff = target - nums[i]
#            for j in range(i+1, len(nums)):
#                if nums[j] == diff:
#                    return [i, j]

        




        
        

