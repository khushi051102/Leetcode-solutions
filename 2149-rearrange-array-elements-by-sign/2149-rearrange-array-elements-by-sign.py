class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n=len(nums)
        result=[0]*n
        pos=0
        neg=1
        for i in nums:
            if i>0:
                result[pos]=i
                pos+=2
            else:
                result[neg]=i
                neg+=2
        return result