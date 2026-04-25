class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums) <= 1:
            return False

        dups = set()

        for i in nums:
            if i in dups:
                return True
            dups.add(i)
        return False


#        for i in range(len(nums)):
#            for j in range(i+1, len(nums)):
#               if nums[i] == nums[j]:
#                    return True
#        return False