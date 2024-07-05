from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        p2=p1 = 0
        s.sort()
        g.sort()

        while p1<len(g) and p2<len(s):
            if g[p1] > s[p2]:
                p2+=1
            elif g[p1] <= s[p2]:
                p2 +=1
                p1 +=1
                res +=1
        return res
            