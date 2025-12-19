class Solution:
    def numTeams(self, scores):
        total = 0
        size = len(scores)

        for mid in range(1, size - 1):
            sl = bl = sr = br = 0

            for left in range(mid):
                if scores[left] < scores[mid]:
                    sl += 1
                elif scores[left] > scores[mid]:
                    bl += 1

            for right in range(mid + 1, size):
                if scores[right] < scores[mid]:
                    sr += 1
                elif scores[right] > scores[mid]:
                    br += 1

            total += sl * br + bl * sr

        return total

if __name__ == "__main__":
    scores = list(map(int, input().strip().split()))
    
    ans = Solution().numTeams(scores)
    print("Number of Teams:", ans)