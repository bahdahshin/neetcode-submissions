class Solution:

    def encode(self, strs: List[str]) -> str:
        import json
        j = json.dumps(strs)
        return j


    def decode(self, s: str) -> List[str]:
        import json
        j = json.loads(s)
        return j