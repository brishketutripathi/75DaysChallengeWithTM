class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsLen = len(nums)
        if numsLen == 0: 
            return -1
        left = [0 for i in range(numsLen)]
        right = [0 for i in range(numsLen)]
        right[numsLen - 1] = nums[numsLen - 1]
        for i in range(numsLen - 2, -1, -1):
            right[i] = right[i + 1] + nums[i]
        left[0] = nums[0]
        if right[0] == left[0]:
            return 0
        for i in range(1, numsLen):
            left[i] = left[i - 1] + nums[i]
            if left[i] == right[i]:
                return i
        return -1
