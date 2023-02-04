n = int(input("Enter Number = "))
a=0
b=1
print("This series will print to ",n," terms")
print("Series = ",a," , ",b)
for i in range(n):
    c=a+b
    a=b
    b=c
    print(" , ",c)
