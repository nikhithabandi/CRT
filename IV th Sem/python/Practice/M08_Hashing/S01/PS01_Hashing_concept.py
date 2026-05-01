# pointer is used to store address
'''
Hashing : It is Array of Ds is ised to store data 
Definition:
Avantages : More Efficent
Hash key Value: Special Key Value
Collision Resolution Technology - Open Hashing , Close Hashing
Open Hashing : Separte Chaining 
Close Hashing: Linear Hashing -  Formula - h(k) = hi(k) % n
,Quadratic Probing, - hi(k) = (hi(k) + i*i)mod m
Double Hashing
Size Should Either We have to take perfect numbers - 5,7,11
''' 
'''a = [10,20,30]
size = 7
table = [None]*size
for i in a:
    index = i % size 
    table[index] = i
print(table)'''