class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r, output = 0, len(heights) - 1, 0

        while l < r:
            output = max(output, (r - l) * min(heights[l], heights[r]))
            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                l += 1
                r -= 1
        return output



        