def findClosestNumber(nums):
    closest = nums[0]
    for num in nums:
        if abs(num) < abs(closest):
            closest = num
        elif abs(num) == abs(closest):
            closest = max(closest, num)
    return closest


nums1 = [-4, -2, 1, 4, 8]
nums2 = [2, -1, 1]
print(findClosestNumber(nums1))  # 输出: 1
print(findClosestNumber(nums2))  # 输出: 1  