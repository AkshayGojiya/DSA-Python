# determine whether there exists a valid binary array original that could have formed derived
class Solution:
    def XOR(self, arr):
        res = 0
        for num in arr:
            res ^= num
        
        return res == 0
    
if __name__ == '__main__':
    arr = [1, 1, 0]
    o = Solution()
    if (o.XOR(arr)):
        print("There exists a valid binary array.")
    else:
        print("No valid binary array exists.")