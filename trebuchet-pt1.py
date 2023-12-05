values = open('calibration-values.txt','r')
lines = values.readlines()
sum = 0

for line in lines:
    nums = [i for i in line if i.isdigit()]

    if len(nums) > 1:
        first = nums[0]
        last = nums[-1]
    else:
        first = nums[0]
        last = nums[0]
    
    n = first + last
    sum += int(n)

print(sum)