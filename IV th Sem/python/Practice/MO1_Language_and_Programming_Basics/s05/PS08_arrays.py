#third max
#nums = list(map(int,input("enter nums").split()))
#if len(set(nums))>=3:
#    print(sorted(set(nums))[-3])
#else:
#    print(max(nums))

#monotonic array
nums=list(map(int,input("enter nums").split()))
int=True
dec=True
for i in range(1,len(nums)):
    if nums[i]>num[i+1]:
        dec = False
    if nums[i]<nums[i+1]:
        dec = False
if inc or dec:
    print("Monotonic Array")
else:
    print("not Monotonic Array")
