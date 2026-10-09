def avg_median(nums:list):
    sum = 0
    avg = 0
    median = 0
    for i in range(0, len(nums)):
        sum += nums[i]
    avg = sum/len(nums)

    i = len(nums)//2
    median = nums[i]
    print(avg)
    print(median)

nums = (2,3,4)
avg_median(nums)
