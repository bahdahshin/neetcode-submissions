class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for _, v in enumerate(strs):
            length = len(v)
            result = result + str(length) + "#" + v

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j = j + 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            result.append(s[i:j])
            i = j

        return result