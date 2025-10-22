def multiply_list(nums):
    product = nums[0]

    for i in range(1, len(nums)):
        product = product * nums[i]

    return product

nums = [1, 2, 3, 4, 5, 6, 7]

print(multiply_list(nums))