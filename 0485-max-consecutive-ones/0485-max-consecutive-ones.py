class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max1=0
        count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
                max1=max(max1,count)
            else:
                count=0
        return max1