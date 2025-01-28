def moveZeroes(nums):
    lastNonZeroIndex = 0  # 记录非零元素的位置
    for i in range(len(nums)):
        if nums[i] != 0:
            # 如果是非零元素，交换到 lastNonZeroIndex 位置
            nums[lastNonZeroIndex], nums[i] = nums[i], nums[lastNonZeroIndex]
            lastNonZeroIndex += 1  # 更新 non-zero 元素的位置

# 示例1
nums1 = [0, 1, 0, 3, 12]
moveZeroes(nums1)
print(nums1)  # 输出: [1, 3, 12, 0, 0]

# 示例2
nums2 = [0]
moveZeroes(nums2)
print(nums2)  # 输出: [0]