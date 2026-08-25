class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        nums.sort()
        print(nums)
        max_len = 1
        start = 0
        for end in range(1, len(nums)):
            print(start, end)
            if nums[end-1] != nums[end]-1:
                max_len = max(max_len, end-start)
                print("max_len", max_len)
                start = end
        
        max_len = max(max_len, len(nums)-start)

        return max_len