class Solution {
    fun maxSubArray(nums: IntArray): Int {
        var opt1_prev = nums[0]
        var opt2_prev = nums[0]

        for (i in 1 until nums.size) {
            opt1_prev = max(opt1_prev + nums[i], nums[i])
            opt2_prev = max(opt2_prev, opt1_prev)
        }

        return opt2_prev
    }
}
