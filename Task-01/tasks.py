#Task 01
a=int(input("Enter First Number:"))
b=int(input("Enter second Number:"))
c=a+b
print("Addition of two numbers is: ",c)

#Task 02
a=int(input("Enter the Number: "))
if a%2==0:
    print("Number is EVEN.")
else:
    print("Number is ODD.")

#Task 03 :- Factorial Calculation
def factorial( a):
    if a==0 or a==1:
        return 1
    else:
        return a*factorial(a-1)
a=int(input("Enter the Number: "))  
print("Factorial is :",factorial(a))

#Task 04 : Fibonacci Sequence
def fibonacci(n):
    if n<=0:
        return[]
    elif n ==1:
        return [0]
    elif n ==2:
        return [0,1]
    else:
        series= fibonacci(n-1)
        series.append(series[-1] + series[-2])
        return series
n=int(input("Enter the Number: ")) 
print("Fibonacci series : ", fibonacci(n))

# Task 05 : Reverse string
def Reverse_String(s):
    return s[::-1]

s=str(input("Enter the string: "))
print("reversed String Is: ",Reverse_String(s))

#Task 06: Palindrom check
def palindrom(word):
    if word == word[::-1]:
        print("Word is palindrom")
    else:
        print("Word is not palindrom")
    
word=str(input("Enter the string: "))
palindrom(word)

# Task 07: Leap year check
def leap_year(year):
    if (year%4==0 and year%100 !=0) or (year%400==0):
        print("Leap Year")
    else:
        print("Not Leap Year")

year=int(input("Enetr the Year: "))
leap_year(year)

#Task 08:Armastrong Number
def Armstrong(Num):
    digits=str(Num)
    power=len(digits)
    total=sum(int(digit)**power for digit in digits)

    if total==Num:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")

Num=int(input("Enter Number:"))
Armstrong(Num)
