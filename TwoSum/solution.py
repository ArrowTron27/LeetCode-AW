class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        returnVal = []
        num = 0
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                num = nums[i] + nums[j]
                if (num == target and i!=j):
                    returnVal.append(i)
                    returnVal.append(j)
                    return returnVal
