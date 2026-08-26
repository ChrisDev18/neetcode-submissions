class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # store best solution ending at i
        opt1 = [float('-inf')  for i in range(n + 1)]
        # store best solution found anywhere up to i
        opt2 = [float('-inf') for i in range(n + 1)]

        for i in range(1, n + 1):
            add_to_subarray = opt1[i - 1] + nums[i - 1]
            start_new = nums[i - 1]
            running_best = opt2[i - 1]
            opt1[i] = max(add_to_subarray, start_new)
            opt2[i] = max(running_best, opt1[i])

        return opt2[n]