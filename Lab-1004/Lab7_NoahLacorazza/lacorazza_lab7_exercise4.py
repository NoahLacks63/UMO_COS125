nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def num_checker(nums, num):
    for n in nums:
        if n == num:
            return True
    
    return False

print(num_checker(nums, 7))