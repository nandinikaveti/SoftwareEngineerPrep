def max_min(nums:list):
    max = 0
    min = 0
    for i in range(0, len(nums)):
        if nums[i] > max:
            max = nums[i]
        return max
        if nums[i] < min:
            min = nums[i]
            return min
nums = (2, 3, 4, 5)
print(max_min(nums))



        