class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        """ 
        Time Complexity O(1) because this problem does not scale to a number, we know it will loop 32 times
        Space Complexity O(1) because this problem only uses variables
        
        Uses logical AND to get the first bit in the integer, then ORs it to the current value of res shifted left
        in order to reverse the integer parameter invoked in the method call

        """
        res = 0

        for i in range(32): # loop for 32 bits 0 -> 32
            bit = (n >> i) & 1  # bit is the bit at the ones place in n(we use AND to get it so it stays the same)
            res = res | (bit << (31 - i)) # res becomes itself shifted to the left by 31 - i then the OR operation is performed on it

        return res # return res