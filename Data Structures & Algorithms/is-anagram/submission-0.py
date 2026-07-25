class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = len(s)
        lt = len(t)

        if ls != lt:
            return False

        ss = sorted(s)
        st = sorted(t)

        if ss == st:
            return True
        
        return False