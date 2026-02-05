class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in nums:
                next_nums = num + 1
                length = 1 
                while next_nums in nums:
                    next_nums += 1
                    length += 1
                longest = max(longest, length)
        return longest