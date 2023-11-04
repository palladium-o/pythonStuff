nums = [3, 1, 2, 5, 1, 5, -7, 9, -8, -3, 3]

diff_list = []

for i in enumerate(nums) - 1:
    if diff < 0:
        diff = nums[1] - nums[0]
    diff_list.append(diff)
    nums.pop(0)

mean = sum(diff_list)/len(diff_list)

print(round(mean, 1))
