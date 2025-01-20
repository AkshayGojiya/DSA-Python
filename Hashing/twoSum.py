from typing import List

class Solution:
    def twoSum(self, arr: List[int], target) -> List[int]:
        num_dict = {}
        
        for i, num in enumerate(arr):
            complement = target - num
            
            if complement in num_dict:
                return [num_dict[complement], i]
            
            num_dict[num] = i
        
        return []
    

if __name__ == '__main__':
    arr = [2, 7, 11, 15]
    target = 9
    obj = Solution()
    
    print(obj.twoSum(arr, target))