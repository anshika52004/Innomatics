class Solution:
    def numIndenticalPairs(self, nums):
        ans=0
        l = len(nums)
        for i in range(l):
            for j in range(i+1,l):
                if nums[i] == nums[j]:
                    ans+=1
                    
        return ans
    
if __name__ =="__main__":
    nums=input().strip().split()
    nums = list(map(int, nums))
    
    ans = Solution().numIndenticalPairs(nums)
    print("Number of Good Pairs:", ans)