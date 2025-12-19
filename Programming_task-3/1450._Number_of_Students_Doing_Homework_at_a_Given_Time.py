class Solution:
    def busyStudent(self, startTime, endTime, queryTime):
        count = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                count += 1
        return count
    
if __name__ == "__main__":
    st = list(map(int, input().strip().split()))
    et = list(map(int, input().strip().split()))
    qt = int(input())
    
    ans = Solution().busyStudent(st, et, qt)
    print("Number of Students Doing Homework at Given Time:", ans)