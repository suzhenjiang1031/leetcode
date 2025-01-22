def maxCoins(piles):
    # 1. 按从大到小排序
    piles.sort(reverse=True)
    
    # 2. 初始化结果
    n = len(piles) // 3
    max_coins = 0
    
    # 3. 选出你的硬币堆，从索引 1 开始，每隔 2 个选择一次
    for i in range(1, 2 * n, 2):
        max_coins += piles[i]
    
    return max_coins

# 示例测试
print(maxCoins([2, 4, 1, 2, 7, 8]))  # 输出: 9
print(maxCoins([2, 4, 5]))           # 输出: 4
print(maxCoins([9, 8, 7, 6, 5, 1, 2, 3, 4]))  # 输出: 18
