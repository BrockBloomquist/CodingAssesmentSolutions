class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        This algorithm uses a sliding window algorithm and a map to keep track of the indexes of the characters and replaces them with the characters
        in the sliding glass window in order to prevent duplicated characters from being in the sliding window.
        Time Complexity: O(n) Space complexity: O(1)
        """
        left,right=0,0
        r = {}
        l = 0
        n = len(s)

        while right < n:
            if s[right] in r:
                left = max(r[s[right]] + 1, left)
                r[s[right]]=right
            else:
                r[s[right]]=right
            l = max(l, (right-left) + 1)
            right += 1

        return l