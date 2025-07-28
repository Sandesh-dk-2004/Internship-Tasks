# Task 09: Prime Number
def prime_num(num):
    if num<=1:
        return False
    
    for i in range(2,int (num**0.5)+1):
        if num% i==0:
            return False
        
    return True

num=int(input("Enter the number: "))
if prime_num(num):
    print("Prime Number.")
else:
    print("not prime Number.")

#Task 10: Sum of Digit.
def sum_of_numbers(n):
    if n==0:
        return 0
    else:
        return n+sum_of_numbers(n-1)
n=int(input("Enter the number for sum: "))
print(f"sum of numbers is:  {sum_of_numbers(n)}")

#Task 11:LCM and GCD
import math
num1= int(input("Enter the first number:"))
num2= int(input("Enter the second number:"))

gcd= math.gcd(num1,num2)
lcm= abs(num1*num2)//gcd

print(f"GCD of {num1} and {num2} is :{gcd}")
print(f"GCD of {num1} and {num2} is :{lcm}")

#Task 12: List Reversal
def Lst_reversal(lst):
    start=0
    end=len(lst)-1
    while start<end:
        lst[start],lst[end] = lst[end],lst[start]
        start +=1
        end -=1
    return lst
mylist=[0,1,2,3,4,5,6,7,8,9]
print("Original List: ", mylist)
print("Reversed List: ", Lst_reversal(mylist))

#Task 13: Sort A List
List=[0,4,5,2,1,8,5,7,4]
sorted_list=sorted(List)
print(f"sorted list is:{sorted_list}")

# Task 14:Remove Duplicates.
def remove_duplicate(lst):
    return list(set(lst))

numbers=[0,0,1,1,45,8,6,1,55,2,4,2,2,8]
print(f"Original list: {numbers}")
print(f"List without duplicates : ",remove_duplicate(numbers))

#Task 15: Length of string
def length_string(str):
    count=0
    for char in str:
        count +=1
    return count
    
str= input("Enter the string: ")
print(f"Length of String is : {length_string(str)}")

#Task 16: Vowels and Consonants
def count_voewels_consonants(str):
    vowels= "aeiouAEIOU"
    vowel_count=0
    consonants_count=0

    for char in str:
        if char.isalpha():
            if char in vowels:
                vowel_count+=1
            else:
                consonants_count+=1

    return vowel_count, consonants_count

str= input("Enter the string: ")
vowel_count, consonants_count= count_voewels_consonants(str)
print(f"vowels counts is: {vowel_count}")
print(f"consonants counts is: {consonants_count}")
