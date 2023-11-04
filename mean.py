nums = [3, 1, 2, 5, 1, 5, -7, 9, -8, -3, 3]

l = len(nums) - 1

diff_list = []

for i in range(l):
    diff = nums[0] - nums[1]
    if diff < 0:
        diff = nums[1] - nums[0]
    diff_list.append(diff)
    nums.pop(0)

mean = sum(diff_list)/len(diff_list)

print(round(mean, 1))
