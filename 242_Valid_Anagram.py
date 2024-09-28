class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s2 = ''.join(sorted(s))
        t2 = ''.join(sorted(t))
        return s2==t2
        