"""
input: XYYX, 2

steps | count | result | maxf | l | r | s[r] | count[s[r]]    | count[s[l]]    | (r - l + 1) - maxf  |
0     | {}    | 0      | 0    | 0 |   |      |                |                |                     |
1     |       |        | 1    | 0 | 0 | X    | key: X, val: 1 | key: X, val: 1 | (0 - 0 + 1) - 1 = 0 |
2     |                |          | 1 | Y    |
3     |                |          | 2 | Y    |
4     |                           | 3 | X    |
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0

        l = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)

        return result
