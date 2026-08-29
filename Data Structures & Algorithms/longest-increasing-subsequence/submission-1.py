class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # opt[i] represents the longest subsequence that ends at nums[i]
        opt = [1 for i in range(len(nums))]
        running_max = 1
        
        # Each iteration will check possible solutions
        # that could include elements up until nums[i]
        for i in range(1, len(nums)):
            # build up opt[i] from all previous opt values opt[j]
            for j in range(0, i):
                # you can only add to subsequence if nums[i] > nums[j]:
                if nums[i] > nums[j]:
                    # opt stores optimal length so assign the max value
                    opt[i] = max(opt[i], opt[j] + 1)
            
            running_max = max(running_max, opt[i])
        
        return running_max