#find the sum of array elements
'''def array_sum(arr):
    total = 0
    for i in arr:
        total += i
    return total
def array_sum(nums):
    s=0
    for i in range(len(nums)-1,-1,-1):
        s+=nums[i]
    return s
print(array_sum([10,20,30,40]))
 # Example
arr = [1, 2, 3, 4, 5]
print("Sum =", array_sum(arr))
'''
#recursive
def array_sum_recursive(nums,i):
    if i==-1:
        return 0
    return nums[i]+array_sum_recursion(nums,i-1)
print(array_sum_recursion([10,20,30,40]))

def array_sum_recursion1(nums):
    if len(nums)==0:
        return 0
    return nums[-1]+array_sum_recursion1(nums[:-1])
print(array_sum_recursion([10,20,30,40]))