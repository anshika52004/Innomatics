class Solution:
    def defang(self, s):
        ans = ""
        for i in s:
            if i == ".":
                ans += "[.]"
            else:
                ans += i
        return ans
    
if __name__ == "__main__":
    s = input()
    
    ans = Solution().defang(s)
    print("Defanged IP Address:", ans)