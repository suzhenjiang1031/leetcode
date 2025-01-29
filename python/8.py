def rotate(nums, k):
    n = len(nums)
    k %= n  # 处理 k > n 的情况
    nums.reverse()  # 翻转整个数组
    nums[:k] = reversed(nums[:k])  # 翻转前 k 个元素
    nums[k:] = reversed(nums[k:])  # 翻转后 n-k 个元素

# 示例测试
nums1 = [1,2,3,4,5,6,7]
rotate(nums1, 3)
print(nums1)  # 输出: [5,6,7,1,2,3,4]

nums2 = [-1,-100,3,99]
rotate(nums2, 2)
print(nums2)  # 输出: [3,99,-1,-100]
