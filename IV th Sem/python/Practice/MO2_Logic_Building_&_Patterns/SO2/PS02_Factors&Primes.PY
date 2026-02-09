#1.read a number from user and count number of factors:
n=int(input("enter a number: "))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
print("numbers of factors:",count)