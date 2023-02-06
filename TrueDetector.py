import random
for i in range(0,2):
    print("""
===================================
Please Enter Two players Name Here.
===================================
""")
    a=str(input("Player 1st = "))
    b=str(input("Player 2nd = "))
    print("Ok Sir ")
    print(a," First you asked question to ",b)
    q1=str(input("Question = "))
    print("Ok ",a," Now ",b," time for answer.")
    a1=str(input("Answer = "))
    per = random.randint(1,100)
    print("The number of correct percentage = ",per)
    if per>50:
        print("Answer is correct")
    else:
        print("Answer is wrong")
    print(b," Now you asked question to ",a)
    q1=str(input("Question = "))
    print("Ok ",b," Now ",a," time for answer.")
    a1=str(input("Answer = "))
    per = random.randint(1,100)
    print("The number of correct percentage = ",per)
    if per>50:
        print("Answer is correct")
    else:
        print("Answer is wrong")
    

