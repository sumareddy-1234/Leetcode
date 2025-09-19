class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set(nums)
        if len(s)<3:
            return max(s)
        else:
            for i in range(2):
                s.remove(max(s))
            return max(s)
        
            

        