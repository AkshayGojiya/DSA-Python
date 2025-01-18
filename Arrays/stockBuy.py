class Solution:
    def maxProfit(self, arr):
        maxProfit = 0
        minPrice = arr[0]

        for i in arr:
            minPrice = min(minPrice, i)
            maxProfit = max(maxProfit, i - minPrice)

        return maxProfit

if __name__ == '__main__':
    arr = [7, 1, 5, 3, 6, 4]
    obj = Solution()
    print("Maximum profit that can be obtained:", obj.maxProfit(arr))