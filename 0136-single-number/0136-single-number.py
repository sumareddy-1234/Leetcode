class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set()
        for i in nums:
            if i in s:
                s.remove(i)
            else:
                s.add(i)
        s=list(s)
        return s[0]
