class Solution:
    def maxSumRangeQuery(self, nums: list[int], requests: list[list[int]]) -> int:
        n = len(nums)
        diff = [0] * (n + 1) 
        for l, r in requests:
            diff[l] += 1
            diff[r + 1] -= 1
        count = []
        running = 0
        for k in range(n):
            running += diff[k]
            count.append(running)    

        count.sort()
        nums.sort()
        return sum(a * b for a, b in zip(nums, count)) % (10**9 + 7)