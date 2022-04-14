def find_max(nums: list) -> int:
    max_num = nums[0]
    for x in nums:
        if x > max_num:
            max_num = x
    return max_num

if __name__ == "__main__":
    print(find_max([2, 4, 9, 7, 19, 94, 5]))