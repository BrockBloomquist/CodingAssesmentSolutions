class Solution(object):
    def countBits(self, n):
        """
        This solution utilizes memoization to calculate and keep track of the number of bits in the solution in order to 
        get the next value because of the repeat of numbers in binary.
        Example:
        0 -> 0000
        1 -> 0001
        2 -> 0010
        3 -> 0011
        4 -> 0100
        5 -> 0101
        ...
        Last 2 bits repeat themselves to get the next values in the sequence which determines an offset to get the values
        rather than recalculating the values. This is a Dynamic solution!
        Offset goes from 1 -> 2 -> 4 -> 8 (doubles everytime or * 2)
        :type n: int
        :rtype: List[int]
        Time Complexity O(n) Space Complexity O(n)
        """
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp