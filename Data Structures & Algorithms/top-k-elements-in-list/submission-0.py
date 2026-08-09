import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num,0) + 1

        freq = [[] for i in range(len(nums) + 1 )]
        for num, cnt in seen.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)

                if len(res) == k:
                    return res
        