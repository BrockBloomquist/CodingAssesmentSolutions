class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Time Complexity: O(1) Space Complexity O(1)
        Uses dictionary to calculate the other value it is looking for and gives it a value of its index which is used to be returned if it is
        needed for the other value to add up to the target
        """
        m = {}

        for i in range(len(nums)):
            if(target - nums[i]) in m:
                return [m[target-nums[i]], i]
            m[nums[i]] = i
        return []