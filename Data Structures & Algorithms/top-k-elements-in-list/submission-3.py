class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # element, frequency of element in nums

        for i in nums:
            count[i] = count.get(i, 0) + 1
            
        sorted_keys = sorted(count.keys(), key=lambda x: count[x], reverse=True)

        res = []
        for key in sorted_keys:
            res.append(key)
            if len(res) == k:
                return res





