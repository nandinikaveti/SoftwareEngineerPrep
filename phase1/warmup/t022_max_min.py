def max_min(nums:list):
    max = nums[0]
    min = nums[0]
    for i in range(0, len(nums)):
        if nums[i] > max:
            max = nums[i]
        elif nums[i]< min:
            min = nums[i]
    print(max)
    print(min)
        
        
nums = (-2, 3, -4, 5, 0)
max_min(nums)



        