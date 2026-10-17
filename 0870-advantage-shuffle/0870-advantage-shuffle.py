class Solution:
    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:
        a=sorted(nums1)
        n=len(nums1)
        order=sorted(range(n) , key=lambda i:nums2[i])
        res=[0]*n
        lo,hi=0,n-1
        for i in a:
            if i>nums2[order[lo]]:
                res[order[lo]]=i
                lo+=1
            else:
                res[order[hi]]=i
                hi-=1
        return res
