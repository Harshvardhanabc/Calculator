for i in range(10000000000):
    print("""
-----------------------------------
Fraction problem solving Calculator
-----------------------------------    
    """)
    print("""
    1. Fraction Addition
    2. Fraction Substraction
    3. Fraction Multiplication
    4. Fraction Dividation
    """)
    Op=int(input("Enter number of applied operation = "))
    if Op==1:
        a=int(input("Enter first fraction nominator number = "))
        b=int(input("Enter first fraction denominator number = "))
        c=int(input("Enter second fraction nominator number = "))
        d=int(input("Enter second fraction denominator number = "))
        add=(a/b)+(c/d)
        print("The Fraction Addition is ",add)
    elif Op==2:
        a=int(input("Enter first fraction nominator number = "))
        b=int(input("Enter first fraction denominator number = "))
        c=int(input("Enter second fraction nominator number = "))
        d=int(input("Enter second fraction denominator number = "))
        sub=(a/b)-(c/d)
        print("The Fraction Substraction is ",sub)
    elif Op==3:
        a=int(input("Enter first fraction nominator number = "))
        b=int(input("Enter first fraction denominator number = "))
        c=int(input("Enter second fraction nominator number = "))
        d=int(input("Enter second fraction denominator number = "))
        Multi=(a/b)*(c/d)
        print("The Fraction Multiplication is ",Multi)
    elif Op==4:
        a=int(input("Enter first fraction nominator number = "))
        b=int(input("Enter first fraction denominator number = "))
        c=int(input("Enter second fraction nominator number = "))
        d=int(input("Enter second fraction denominator number = "))
        Div=(a/b)/(c/d)
        print("The Fraction Dividation is ",Div)
    else:
        print("Sorry invalid Entry!")