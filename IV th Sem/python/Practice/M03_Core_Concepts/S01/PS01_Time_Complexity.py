'''Time Complexity:
Time Complexity can be measure based upon the input
ex:
n=10
print(n)
O(1)-->constant time
O(n)-->single loop
O(n^2)-->two loops
O(log n)-->
'''
#print("Time Complexity:")
#arr = [1,2,3,4,5]
#Brute Force -->step by step execute,high complexityneglects the efficiency
# Optimal Solution -->needs thinking ,low complexity
'''def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
print(linear_search([10,20,30,58,46],10))
print(linear_search([10,20,30,58,46],46))
print(linear_search([10,20,30,58,46],30))
'''
def binary_search(arr,target):
    for i in range(len(arr)):
        low=0
        high=len(arr-1)