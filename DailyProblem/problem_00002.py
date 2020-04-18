n =  [3,2,1]

def product(nums):
    n = len(nums)
    left = [1] * n
    right = left.copy()

    for i in range(1,n):
        left[i] = left[i-1] * nums[i-1]

    for i in range(n-2,-1,-1):
        right[i] = right[i+1] * nums[i+1]
        
    for i in range(n):
        left[i] = left[i] * right[i]

    return left

print(product(n))