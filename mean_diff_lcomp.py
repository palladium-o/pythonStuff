nums = [3, 1, 2, 5, 1, 5, -7, 9, -8, -3, 3]

diff_list = [
   abs(a - b)
   for a, b in zip(nums, nums[1:])
]

mean = sum(diff_list) / len(diff_list)

print(f'Mean: {mean:.1f}')
