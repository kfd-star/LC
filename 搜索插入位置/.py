class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n =len(nums)
        left = 0
        right = n - 1
        ans = n
        while (left <= right) :
            mid = ((right - left) >> 1) + left
            if (target <= nums[mid]) :
                ans = mid
                right = mid - 1
            else :
                left = mid + 1
        return ans
