class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # calculate all possible (unsorted) triples
        triples = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # if j == i:
                #     continue
                for k in range(j+1, len(nums)):
                    # if k == i or k == j:
                    #     continue
                    triple = nums[i], nums[j], nums[k]

                    if sum(triple) == 0:
                        triples.add((nums[i], nums[j], nums[k]))

        return [list(triple) for triple in triples]