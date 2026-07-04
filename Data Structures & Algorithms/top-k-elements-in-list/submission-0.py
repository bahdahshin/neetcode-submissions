import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        heap = []
        result = []

        for i, v in enumerate(nums):
            if v not in hashmap:
                hashmap[v] = 0
            else:
                hashmap[v] = hashmap[v] + 1
            
        for key, val in hashmap.items():
            heapq.heappush(heap, (-val, key))

        for i in range(k):
            item = heapq.heappop(heap)
            result.append(item[1])

        return result