from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running = []
        curr_sum = 0
        for num in nums:
            curr_sum += num
            running.append(curr_sum)
        return running

if __name__ == "__main__":
    nums = [1, 2, 3, 4]

    # sol = Solution()
    result = Solution().runningSum(nums)

    print("Input:", nums)
    print("Running Sum:", result)
