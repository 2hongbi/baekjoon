def sum_elements(nums):
    if len(nums) == 1:
        return nums[0]
    return nums[0] + sum_elements(nums[1:])


if __name__ == '__main__':
    print(sum_elements([1, 2, 3, 4, 5]))