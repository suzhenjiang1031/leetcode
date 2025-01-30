def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n
    
    # Calculate prefix products
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]
    
    # Calculate suffix products and multiply with prefix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]
    
    return answer
