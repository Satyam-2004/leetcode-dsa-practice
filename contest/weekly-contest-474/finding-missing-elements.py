class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums = sorted(set(nums))
        min_val = nums[0]
        max_val = nums[-1]

        r1 = set(range(min_val, max_val + 1))
        r2 = set(nums)
        res = sorted(r1 - r2)
        return res
