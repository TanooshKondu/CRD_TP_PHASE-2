#Bubble sort

def performBubbleSort(nums):
    n = len(nums)
    fixThisPosition = n -1
    
    while fixThisPosition > 0:
        for index in range(0, fixThisPosition):
            if nums[index] > nums[index+1]:
                nums[index], nums[index+1] = nums[index+1], nums[index]
        print(nums)
        fixThisPosition -= 1
nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Before Sorting: ", nums)
performBubbleSort(nums)
print("After sorting: ", nums)