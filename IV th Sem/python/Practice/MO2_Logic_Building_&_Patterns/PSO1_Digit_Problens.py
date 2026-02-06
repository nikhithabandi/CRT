n=int(input("enter num:"))
count=0
while n>0:
    n=n//10
    count+=1
print("the num of digits in the given num is:",count)