class Solution:
    def subtractProductAndSum(self, n):
        p = 1
        s = 0
        while n:
            a = n%10
            s += a
            p *= a
            n //=10
        return p-s
    
if __name__ == "__main__":
    n = int(input())
    
    ans = Solution().subtractProductAndSum(n)
    print("Subtract the Product and Sum of Digits:", ans)