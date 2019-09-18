class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        s1 = min(strs)
        s2 = max(strs)
        print(s1)
        print(s2)
        # for key, value in enumerate(s1):
        #     if value != s2[key]:
        #         return s2[:key]
        # return s1
        
if __name__ == "__main__":
    s = ["flower","flow","floight"]
    res = Solution()
    str = res.longestCommonPrefix(s)
    # print(str)
