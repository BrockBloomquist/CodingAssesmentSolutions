# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        Uses the guess API to get if the value is higher or lower in order to perform a binary search on guesses
        """
        low = 1
        high = n
        mid = 0
        while low <= high:
            mid = (high + low) // 2
            g = guess(mid)
            if g == 0:
                return mid
            elif g == -1:
                high = mid - 1
            elif g == 1:
                low = mid + 1