class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = {}
        max_len = 0
        current_len = 0

        if s == "":
            return 0
        for i in range(len(s)):
            x = s[i]
            if x in hash:
                m = hash[x]
                for j in range((i-current_len),(hash[x]+1)):
                    hash.pop(s[j])
                current_len = i-m-1
            current_len += 1
            if current_len > max_len:
                max_len = current_len
            if i == len(s)-1:
                return max_len
            hash[x] = i