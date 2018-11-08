into = """
Choose an action:
1 - Addition
2 - Subtraction
3 - Multiplication
4 - Division
"""

print(into)

choosed = int(input("Enter an action number: "))

if choosed == 1:
   ch1  = int(input("Enter the first number: "))
   ch2  = int(input("Enter the second number: "))
   print("Result:{} + {} = {} ".format(ch1, ch2, ch1+ch2))  
elif choosed == 2:
   ch1  = int(input("Enter the first number: "))
   ch2  = int(input("Enter the second number: "))
   print("Result:{} - {} = {} ".format(ch1, ch2, ch1-ch2))
elif choosed == 3:
   ch1  = int(input("Enter the first number: "))
   ch2  = int(input("Enter the second number: "))
   print("Result:{} * {} = {} ".format(ch1, ch2, ch1*ch2))   
elif choosed == 4:
   ch1  = int(input("Enter the first number: "))
   ch2  = int(input("Enter the second number: "))
   print("Result:{} / {} = {} ".format(ch1, ch2, ch1/ch2))
else:
    print(" == "*20)
    print("Wrong choice")
    print(" == "*20)
    print(into)


