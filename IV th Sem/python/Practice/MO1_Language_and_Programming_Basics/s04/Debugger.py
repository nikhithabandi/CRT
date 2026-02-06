#finding and fixing of errors
#types of errors:
#1.syntax errors-->missing of colon,missing of IndentationError
#2.runtime error-->division by zero
#3.logical error-->missing of logics

#Debugging Techniques:
#1.print()
#2.try-except
#3.using pdb
    #pdb-->python debugger
    #purpose:
    #1.pause the execution code
    #2.inspect the variables values
    #3.to run the code line by line
#pdb Commands:
#1.n-->to execute the output in a next line
#2.p variable-->to get the value of a variable
#3.l-->list nearby code
#4.c-->continue the execution
#5.s-->to start a function
#6.r-->return from the function
#7.h-->help
#8.q-->quit the execution

try:
    a=int(input("enter a num: "))
    print(10/a)
except ZeroDivisionError:
    print('Can not divisible by Zero.')
except ValueError:
    print("Invalid input")

import pdb
def add(a,b):
    pdb.set_trace() #set the breakpoint
    return a+b
a=int(input("enter a num: "))
b=int(input("enter a num: "))
print(add(a,b))