class Solution(object):

    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        """
        something things i noticed
        1) the number of piles can not be higher than the number of hours
        2) if the number of piles and hours are the same, k autmoaticly beomces the largest ith value
        3) the more hours, the smaller k needs to be
        thus my program would need to find the largest values quickly
        """
        i , j = 1, max(piles)
        res = max(piles)
        while i <=j:
            m = (i+j)//2
            total = 0
            for x in piles:
                total = total + (x+m-1)//m
            if total <= h:
                print(total)
                res = min(res, m)
                j = m -1
            else:
                i = m + 1
        return res
