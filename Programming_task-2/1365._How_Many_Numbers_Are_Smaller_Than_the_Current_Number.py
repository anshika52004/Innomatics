class Solution:
    def smallerNumbersThanCurrent(self, nums):
        ans=[]
        for i in nums:
            c=0
            for j in nums:
                if i>j:
                    c+=1
            ans.append(c)
        return ans
    
if __name__ == "__main__":
    nums = input().strip().split()
    nums = list(map(int, nums))
    
    ans = Solution().smallerNumbersThanCurrent(nums)
    print("Numbers smaller than the current number:", ans)