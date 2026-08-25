class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        alt = set(nums)

        return len(alt) != len(nums)