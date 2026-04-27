class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        output = []

        for i in range(len(sortedNums)):
            if i > 0 and sortedNums[i] == sortedNums[i - 1]:
                continue

            left, right = i + 1, len(sortedNums) - 1
            while left < right:
                threeSum = sortedNums[i] + sortedNums[left] + sortedNums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    output.append([sortedNums[i], sortedNums[left], sortedNums[right]])
                    left += 1
                    while sortedNums[left] == sortedNums[left - 1] and left < right:
                        left += 1
                
        
        return output


                     