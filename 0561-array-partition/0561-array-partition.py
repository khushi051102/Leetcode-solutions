class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        new=sorted(nums)
        total=0
        i=0
        while i<len(new):
            total+=new[i]
            i+=2
        return total
