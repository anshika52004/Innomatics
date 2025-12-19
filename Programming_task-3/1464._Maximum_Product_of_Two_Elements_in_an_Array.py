class Solution:
    def maxProduct(self, nums):
        a = 0
        b = 0
        for i in nums:
            if i>a:
                b=a
                a=i
            elif i>b:
                b=i
        return (a-1)*(b-1)

if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    
    ans = Solution().maxProduct(nums)
    print("Maximum Product of Two Elements in an Array:", ans)