class Solution {
    fun maxSubArray(nums: IntArray): Int {
        val n = nums.size
        
        val opt1 = IntArray(n)
        val opt2 = IntArray(n)

        opt1[0] = nums[0]
        opt2[0] = nums[0]

        for (i in 1 until n) {
            opt1[i] = max(opt1[i - 1] + nums[i], nums[i])
            opt2[i] = max(opt2[i - 1], opt1[i])
        }

        return opt2[n-1]
    }
}
