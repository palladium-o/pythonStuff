nums = [3, 1, 2, 5, 1, 5, -7, 9, -8, -3, 3]

diff_list = []

while len(nums) > 1:
    diff = abs(nums[0] - nums[1])
    diff_list.append(diff)
    nums.pop(0)

mean = sum(diff_list) / len(diff_list)

print(f'Mean: {mean:.1f}')
