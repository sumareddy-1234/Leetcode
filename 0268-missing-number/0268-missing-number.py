class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j=0
        for i in range(len(nums)+1):
            if j in nums:
                j+=1
            else:
                return j
            
