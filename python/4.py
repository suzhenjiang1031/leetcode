def twoSum(nums, target):
    num_map = {}  # 创建一个空的哈希表
    for i, num in enumerate(nums):
        complement = target - num  # 计算需要的另一个数
        if complement in num_map:  # 检查是否在哈希表中
            return [num_map[complement], i]  # 返回两个数的索引
        num_map[num] = i  # 将当前数及其索引存入哈希表
    return []  # 如果没有找到，返回空列表（根据题目描述，这种情况不会发生）
    
# 示例测试
print(twoSum([2, 7, 11, 15], 9))  # 输出: [0, 1]
print(twoSum([3, 2, 4], 6))       # 输出: [1, 2]
print(twoSum([3, 3], 6))          # 输出: [0, 1]