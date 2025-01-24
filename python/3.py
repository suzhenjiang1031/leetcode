import heapq

def maxValueOfCoins(piles, k):
    dp = [0] * (k + 1)
    for pile in piles:
        for i in range(k, -1, -1):
            total = 0
            for j in range(min(len(pile), k - i)):
                total += pile[j]
                dp[i + j + 1] = max(dp[i + j + 1], dp[i] + total)
    return dp[k]

# 示例 1
piles = [[1, 100, 3], [7, 8, 9]]
k = 2
print(maxValueOfCoins(piles, k))  # 输出: 101

# 示例 2
piles = [[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]]
k = 7
print(maxValueOfCoins(piles, k))  # 输出: 706


