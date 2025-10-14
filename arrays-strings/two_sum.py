class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashy = {}
        for index, num in enumerate(nums):
            complement = target - num 
            if complement in hashy:
                return [hashy[complement], index]
            hashy[num] = index