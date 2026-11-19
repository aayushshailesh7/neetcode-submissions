class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        val = {}
        for x in s:
            if x in val:
                val[x] = val.get(x) + 1
            else :
                val[x] = 1
        for y in t:
            if y in val:
                val[y] = val.get(y) - 1
            else: 
                return False
            if val[y] < 0:
                return False
        return True