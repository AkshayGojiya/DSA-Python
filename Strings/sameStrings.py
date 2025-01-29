class Solution:
    def isStringsSame(self, s1, s2):
        return s1 == s2
    

if __name__ == '__main__':
    s1 = "listen"
    s2 = "silent"
    obj = Solution()
    print(obj.isStringsSame(s1, s2))