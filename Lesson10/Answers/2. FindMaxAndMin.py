str = input("Please enter at least 5 comma delimited numbers: ")

nums = []
for s in str.split(','):
    nums.append(int(s))

# 12, 3, 4, 5, 45, 21, -24, 12, 4, 5
max = nums[0]
min = nums[0]
for x in nums:
    if max < x:
        max = x
    if min > x:
        min = x

print('The smallest number is', min, ', the biggest number is', max)
