class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = len(s)
        lt = len(t)

        if ls != lt:
            return False

        ds = {}
        dt = {}

        for x in s:
            if x not in ds:
                ds[x] = 1
            else:
                ds.update({x:ds[x]+1})

        for y in t:
            if y not in ds:
                return False
            elif y in ds:
                ds.update({y:ds[y]-1})
            
            if ds[y] < 0:
                return False

        return True



