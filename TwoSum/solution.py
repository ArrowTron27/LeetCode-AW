class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # This is the return value array
        returnVal = []
        
        #number to add up the 2 sums
        num = 0
        
        
        # Nested for loop to search arrays
        for i in range(len(nums)):
            for j in range(len(nums)):
                # Get the num of the array indexes
                num = nums[i] + nums[j]
                if (num == target and i!=j): # If num = target, and i and j are not the same index
                    # Add to the return value array
                    returnVal.append(i)
                    returnVal.append(j)
                    return returnVal
