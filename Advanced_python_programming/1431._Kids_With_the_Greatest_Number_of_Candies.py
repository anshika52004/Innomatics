from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        ans = []
        for candy in candies:
            ans.append(candy + extraCandies >= max_candy)
        return ans

if __name__ == "__main__":
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3

    sol = Solution()
    result = sol.kidsWithCandies(candies, extraCandies)

    print("Candies:", candies)
    print("Extra Candies:", extraCandies)
    print("Result:", result)
