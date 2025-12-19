class Solution:
    def countBits(self, n):
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
    
if __name__ == "__main__":
    n = int(input())
    
    ans= Solution().countBits(n)
    print("Counting Bits:", ans)