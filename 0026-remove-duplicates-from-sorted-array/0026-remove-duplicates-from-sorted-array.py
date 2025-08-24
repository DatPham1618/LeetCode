class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        for current in range(1, len(nums)):
            if nums[k - 1] != nums[current]:
                nums[k] = nums[current]
                k += 1

        return k