class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        c = Counter(nums)
        h = []
        for kk, vv in c.items():
            heapq.heappush(h, (-vv, kk))
            
        res = []
        for _ in range(k):
            i = heapq.heappop(h)
            res.append(i[1])
        return res