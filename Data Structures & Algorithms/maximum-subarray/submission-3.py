class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # store best solution ending at i
        opt1 = [0 for i in range(n)]
        # store best solution found anywhere up to i
        opt2 = [0 for i in range(n)]

        opt1[0] = nums[0]
        opt2[0] = nums[0]

        for i in range(1, n):
            opt1[i] = max(opt1[i - 1] + nums[i], nums[i])
            opt2[i] = max(opt2[i - 1], opt1[i])

        return opt2[n-1]