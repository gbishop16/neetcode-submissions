class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # element, frequency of element in nums
        freq = [[] for i in range(len(nums) + 1)]


        for i in nums:
            count[i] = count.get(i, 0) + 1
        for i, c in count.items():
            freq[c].append(i)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


        # sorted_keys = sorted(count.keys(), key=lambda x: count[x], reverse=True)

        # res = []
        # for key in sorted_keys:
        #     res.append(key)
        #     if len(res) == k:
        #         return res





