class Solution:

    def encode(self, strs: List[str]) -> str:
        import json
        j = json.dumps(strs)
        print(1, j)
        return j


    def decode(self, s: str) -> List[str]:
        import json
        print(2, s)
        j = json.loads(s)
        print(3, j)
        return j