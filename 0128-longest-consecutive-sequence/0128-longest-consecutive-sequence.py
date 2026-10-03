class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        nums=set(nums)
        best=0
        for x in nums:
            if x-1 not in nums:
                current=1
                i=x
                while i+1 in nums :
                    current+=1
                    i+=1
                best=max(current,best)
        return best