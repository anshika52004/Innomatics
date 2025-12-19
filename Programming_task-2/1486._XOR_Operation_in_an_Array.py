class Solution:
    def xorOperation(self, n, start):
        ans = 0
        for i in range(n):
            ans ^= (start + 2 * i)
        return ans
    
if __name__ == "__main__":
    n = int(input())
    s = int(input())
    
    ans = Solution().xorOperation(n, s)
    print("XOR Operation Result:", ans)