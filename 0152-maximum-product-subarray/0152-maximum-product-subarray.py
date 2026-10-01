class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        prefix, suffix = 1, 1
        best = float('-inf')
        for i in range(n):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            prefix *= nums[i]
            suffix *= nums[n - 1 - i]
            best = max(best, prefix, suffix)
        return best