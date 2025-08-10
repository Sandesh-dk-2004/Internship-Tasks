#Task 17:Table of a Number
def table_of_number(num):
    for i in range(1,11):
        op= i*num
        print(f"{i}*{num} = {op}")
        i +=1
num=int(input("Enter the number: "))
table_of_number(num)

# Task 18: Swap two numbers
def swap_numbers(num1,num2):
    num1,num2=num2,num1
    print(f"Numbers after swapping: {num1} and {num2}")

num1=int(input("Enter first number: "))
num2=int(input("Enter Second number: "))
swap_numbers(num1,num2)

#Task 19: Check substring
def Check_Substring(substr,text):
    if substr in text:
        print(f"{text} contains {substr}")
    else:
        print(f"{text} not contains {substr}")

text=input("Enter the text: ")
substr=input("Enter the substring: ")
Check_Substring(substr,text)

#Task 20:Decimal to binary conversion.
def DecimalToBinary(number):
    Binary=bin(number).replace("0b","")
    print(f"Binary convergene of {number} is :{Binary}")

number=int(input("Enter the Decimal Number: "))
DecimalToBinary(number)

#Task 21:
def addition_Of_Matrix(metrix1,metrix2):

    if len(metrix1) != len(metrix2) or len(metrix1[0]) != len(metrix2[0]):  
        raise ValueError("Matrix Must be Have the same dimentions")

    rows= len(metrix1)
    colms=len(metrix1[0])
    result = [[0 for _ in range(colms)] for _ in range(rows)]

    for i in range (rows):
        for j in range (colms):
            result [i][j] = metrix1[i][j] +  metrix2[i][j]

    return result

metrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

metrix2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

sum_matrix= addition_Of_Matrix(metrix1,metrix2)
print("Resultant matrix : ")
for row in sum_matrix:
    print(row)

#Task 22: Matrix Multiplication 
def matrix_multiplication(matrix01,matrix02):
    
    if len(matrix01[0]) != len(matrix02):
        raise ValueError("Column of matrx A should  be equlas to the Rows of the Matrix B")
    
    result_rows= len(matrix01)
    result_cols=len(matrix02[0])

    result = [[0 for _ in range(result_cols)] for _ in range(result_rows)]

    for i in range(result_rows):
        for j in range(result_cols):
            for k in range(len(matrix02)):
                result[i][j] += matrix01[i][k] * matrix02[k][j]

    return result

matrix01 = [[1, 2, 3],
     [4, 5, 6]]

matrix02 = [[7, 8],
     [9, 10],
     [11, 12]]
product_matrix=matrix_multiplication(matrix01,matrix02)
print("Product of Matrices is: ")
for row in product_matrix:
      print(row)

#Task 23: find the second largest number.

def second_Largest_num(lst):
    sorted_lst= sorted(set(lst))
    print(sorted_lst)
    if len(sorted_lst) <= 2:
        print("No second largest number exists.")
    else:
        print(f"second largest number from the list is : {sorted_lst[-2]}")

lst=[0,8,75,4,2,9,5,4,7,3,2,14,56,78]
second_Largest_num(lst)

#Task 24: Check Anagrams.
def Check_anagrams(strg1,strg2):
    if sorted(strg1)== sorted(strg2):
        print("String are anagrams.")
    else:
        print("Not anagrmas.")

strg1= input("Enter the First String: ")
strg2= input("Enter the Second String: ")
Check_anagrams(strg1,strg2)