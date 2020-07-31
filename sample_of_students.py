import math
a=int(input("Enter 1st number="))
b=int(input("Enter 2nd number="))
print ("A=" ,a," ","B=",b)
operator=input("Enter any of the operator [+,-,*,/]")
if operator=='+':
    print (a+b)
elif operator=='-':
    print (a-b)
elif operator=='*':
    print (a*b)
elif operator=='/':
    print (a/b)
else:
    print ("Invalid Operator")
c=input("Do you wanna continue to calculate factorial [Y/N]").capitalize()
if c=='Y':
    d=int(input("Enter a number for factorial :"))
    # print(d)
    # fact=1
    # if d<0:
    #     print("Sorry, Factorial does not exist")
    # elif d==0:
    #     print("The factorial is 1")
    # else:
    #     for i in range(1,d+1):
    #         fact=fact*i
    #     print("The factorial of ",d," is ",fact)
    fact = math.factorial(d)
    print(f"The factorial of {d} is {fact}")
elif c=='N':
    print("Ok Thanks")
else:
    print("Wrong Entry")
