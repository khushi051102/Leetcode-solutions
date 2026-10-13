class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        new=sorted(nums)
        x=[]
        i=0
        while i<len(new):
            j=min(new[i],new[i+1])
            x.append(j)
            i+=2
        return sum(x)
