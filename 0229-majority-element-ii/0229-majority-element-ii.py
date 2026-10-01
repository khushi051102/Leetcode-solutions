class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        cand1, cand2 = None, None
        count1, count2 = 0, 0
        for x in nums:
            if x == cand1:
                count1 += 1
            elif x == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = x, 1
            elif count2 == 0:
                cand2, count2 = x, 1
            else:
                count1 -= 1  
                count2 -= 1

        result = []
        for c in (cand1, cand2):
            if c is not None and nums.count(c) > len(nums) // 3:
                result.append(c)
        return result