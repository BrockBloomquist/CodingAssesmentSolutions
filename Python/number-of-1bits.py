class Solution(object):
    def hammingWeight(self, n):
        """
        The hamming weight counts the number of active (1) input bits in a given input.
        This solution loops from 0-32 exclusive by taking the right most bit and evaluating if it is equal to 1, if yes then a count
        variable increases by 1 then uses the shift right bitwise operator to move to the next bit. 
        Time Complexity O(1) Space complexity O(1)
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(32):
            bit = n & 1
            n = n >> 1
            if bit == 1:
                count += 1
        return count