class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            nums[i + 1] = nums[i] + nums[i + 1]
        
        return nums