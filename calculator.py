for i in range(10000000000000):
    print("""
-------------------------------------
Calculator for two digits operations
-------------------------------------
""")

    print("""
1. Addition
2. Substraction
3. Multiplication
4. Dividation
""")

    OP=int(input("Enter Number which operation would you like to apply = "))
    if(OP==1):
        x=int(input("First Number = "))
        y=int(input("First Number = "))
        Add = x+y
        print("Addition is ",Add)
    elif(OP==2):
        x=int(input("First Number = "))
        y=int(input("First Number = "))
        Sub = x-y
        print("Substraction is ",Sub)
    elif(OP==3):
        x=int(input("First Number = "))
        y=int(input("First Number = "))
        Multi = x*y
        print("Multiplication is ",Multi)
    elif(OP==4):
        x=int(input("First Number = "))
        y=int(input("First Number = "))
        Div = x/y
        print("Dividation is ",Div)
    else:
        print("Sorry invalid Operation")
