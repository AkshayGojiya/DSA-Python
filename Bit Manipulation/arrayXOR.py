class Solution:
    def XOR(self, arr):
        res = 0
        for num in arr:
            res ^= num
        return res
    
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    obj = Solution()
    print("XOR of all numbers in the array:", obj.XOR(arr))