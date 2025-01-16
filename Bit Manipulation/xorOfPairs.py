from typing import List

class Solution:
    def xor_all_pairs(self,nums1: List[int], nums2: List[int]) -> int:
        res = 0

        if len(nums2) % 2:
            for num in nums1:
                res ^= num
        
        if len(nums1) % 2:
            for num in nums2:
                res ^= num

        return res
    

if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [5, 6, 7, 8]
    print("Bitwise XOR of All Pairings :",solution.xor_all_pairs(nums1, nums2))