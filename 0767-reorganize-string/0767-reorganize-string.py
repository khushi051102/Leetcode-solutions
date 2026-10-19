class Solution:
    from collections import Counter
    def reorganizeString(self, s: str) -> str:
        freq=Counter(s)
        n=len(s)
        if max(freq.values())>(n+1)//2:
            return ""
        res=[""]*n
        idx=0
        for c,value in freq.most_common():
            for _ in range(value):
                res[idx]=c
                idx+=2
                if idx>=n:
                    idx=1
        return "".join(res)