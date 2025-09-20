class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        s=[]
        j=1
        while len(s)!=k:
            if j not in arr:
                s.append(j)
            j+=1
        return s[k-1]

        