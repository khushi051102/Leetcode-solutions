class Solution:
    from collections import Counter
    def rearrangeBarcodes(self, barcodes: list[int]) -> list[int]:
        freq=Counter(barcodes)
        res=[0]*len(barcodes)
        idx=0
        for i,value in freq.most_common():
            for _ in range(value):
                res[idx]=i
                idx+=2
                if idx>=len(barcodes):
                    idx=1
        return res