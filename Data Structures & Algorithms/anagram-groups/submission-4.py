class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hashmap = {}

        for _, v in enumerate(strs):
            encode = [0] * 26
            
            for _, vv in enumerate(v):
                num = ord(vv) - ord("a")
                encode[num] = encode[num] + 1
            
            if str(encode) not in hashmap:
                hashmap[str(encode)] = []
            hashmap[str(encode)].append(v)

        for key, val in hashmap.items():
            result.append(val)
        
        return result