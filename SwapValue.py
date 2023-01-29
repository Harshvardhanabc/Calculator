"""
-------------------------------------
Swap two values by using two variable
-------------------------------------
"""
x=int(input("Enter first value = "))
y=int(input("Enter second value = "))
print("Entered values are ",x," and ",y)
x=x+y
y=x-y
x=x-y
print("After swaping values are ",x," and ",y)