class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        Since the substring break the moment a letter is repeated what i could do is have a hashset,
        """
        if s == " ":
            return 0 
        thisset = set()
        count = 0
        ret = 0
        for x in range(len(s)):
            while s[x] in thisset:
                thisset.remove(s[count])
                count +=1
            thisset.add(s[x])
            ret = max(x-count+1, ret)
            print(thisset, ret)
        return ret
