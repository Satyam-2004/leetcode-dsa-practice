class Solution:
    def maxproduct(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 3:
            return 0

        nums.sort()

        cand1 = 100000 * nums[-1] * nums[-2] 

        cand2 = 100000 * nums[0] * nums[1]

        res = max(cand1, cand2)

        if n >= 2 and nums[0] < 0 and nums[1] < 0:
            cand2 = 100000 * nums[0] * nums[1]
            res = max(res, cand2)
        
        return res
