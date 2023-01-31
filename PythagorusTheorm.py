import math
print("""
=======================================
Pythagorus theorm Use in Python Program
=======================================
""")
a=int(input("Heigt = "))
b=int(input("Base = "))
c=int(input("Hypotenious = "))
if c==0:
    c=(a*a+b*b)
    c=math.isqrt(c)
    print("Answer = ",c)
elif a==0:
    a=(c*c-b*b)
    a=math.isqrt(a)
    print("Answer = ",a)
elif b==0:
    b=(c*c-a*a)
    b=math.isqrt(b)
    print("Answer = ",b)
else:
    print("No answer")