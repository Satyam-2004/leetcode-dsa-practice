from math import ceil

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=abs, reverse=True)
        n = len(nums)
        k = (n + 1) // 2  # number of positive terms
        pos_sum = sum(x * x for x in nums[:k])
        neg_sum = sum(x * x for x in nums[k:])
        return pos_sum - neg_sum