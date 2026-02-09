#1.count the digits of numbers:
#n=int(input("enter num:"))
#count=0
#while n>0:
#    n=n//10
#    count+=1
#print("the num of digits in the given num is:",count)

#2.sum of the digits of a number:
#n=int(input("enter a number: "))
#sum=0
#while n>0:
#   digit=n%10
#    sum=sum+digit
#    n=n//10
#print("sum of digits:",sum)

#3.product of the number:
#n=int(input("enter a number:"))
#product=1
#while n>0:
#    digit=n%10
#    product=product*digit
#    n=n//10
#print("product of a number:",product)

#4.reverse the number:
#n=int(input("enter a number: "))
#rev=0
#while n>0:
#    digit=n%10
#    rev=rev*10+digit
#    n=n//10
#print("Reversed number: ",rev)
#      (or)
#str ="python"
#reversed_str=str[::-1]
#print(reversed_str)


#5.print the largest digit of a number
#n=int(input("enter a number: "))
#max_digit=0
#while n>0:
#    digit=n%10
#    if digit>max_digit:
#        max_digit=digit
#    n=n//10
#print("largest digit: ",max_digit)

#6.count the even and odd digits:
n=int(input("enter a number: "))
even = 0
odd = 0
while n>0:
    digit=n%10
    if digit%2==0:
        even+=1
    else:
        odd+=1
    n=n//10
print("even digits: ",even)
print("odd digit: ",odd)