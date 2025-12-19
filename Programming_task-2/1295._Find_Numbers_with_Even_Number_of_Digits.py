class Solution:
    def findnumbers(self, nums):
        c=0
        for i in nums:
            if (self.countdigits(i)):
                c+=1
        return c
        
    def countdigits(self, n):
        count=0
        while n:
            count+=1
            n//=10
        return count&1==0
    
    
if __name__ == "__main__":
    nums=input()
    
    ans = Solution().findnumbers(nums)
    print("Count of numbers with even number of digits:", ans)