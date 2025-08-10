#task 25: Find the Missing Number.
'''def find_missing_no(nums):
     n=len(nums)
     expected_sum=((n+1)*(n+2)) // 2
     actual_sum= sum(nums)
     return actual_sum-expected_sum

nums=list(map(int, input("enter the umbers seperated by space : ").split()))

missing= find_missing_no(nums)
print(f"Missing Number is : {missing}")

#Task 26: Check Balanced Paranthesis.
def is_balanced_paranthesis(s):
    stack=[]
    pairs={')':'(',']':'[','}':'{'}

    for char in s:
        if char in "(,[,{":
            stack.append(char)
        elif char in "),],}":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return not stack

string=input("Enter the String Parenthesis :")
if is_balanced_paranthesis(string):
    print("Paranthesis is balanced.")
else:
    print("Paranthesis is not balanced.")

#Task 27: Lohgest word in sentence

def longest_word(sentence):
    word= sentence.split()
    longest=max(word, key=len)
    return longest

sentence=input("Enter the sentence : ")
print(f"Longest word is: {longest_word(sentence)}")

# Task 28:Count words in Sentence.
def word_count(Sentence):
    word=Sentence.split()
    return len(word)

Sentence=input("Enter the sentence : ")
print(f"Number Of Words; {word_count(Sentence)}")

#Task 29:Check Pythagorean Triplet
def check_pythagorean_triplet(a,b,c):
    sides=sorted([a,b,c])
    a,b,c=sides
    return a**2+b**2==c**2

a,b,c =map(int ,input("Enter the values of sides sepearted by space: ").split())

if check_pythagorean_triplet(a,b,c):
    print("they form pythagorean triplet.")

else:
    print("They not form pythagorean triplet. ")

# Task 30: bubble sort.
def bubble_sort(nums):
    n=len(nums)
    for i in range(n):
        for j in range(0,n-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums

nums= list(map(int,input("Enter the Numbers seperated by space : ").split()))

sorted_nums=bubble_sort(nums)
print(f"Sorted List : {sorted_nums}")

#Task 31: Binary Search.
def Binary_search(nums, target):
    left, right = 0 ,len(nums)-1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid]== target:
            return mid
        elif nums[mid] < target:
            left = mid + 1   
        else: 
            right = mid - 1

    return -1

nums = list(map(int, input("Enter the list if numbers seperated by space : ").split())) 
target= int(input("Enter the target number : "))

index= Binary_search(nums,target)
if index != -1:
    print(f"Target found at index {index}")

else:
    print(f"Target Not found")'''

#Task 32:
def find_subarray_with_sum(nums, target):
    start = 0
    current_sum = 0

    for end in range(len(nums)):
        current_sum += nums[end]
        while current_sum > target and start <= end:
            current_sum -= nums[start]
            start += 1

        if current_sum == target:
            return (start, end)  
    return -1  

nums = list(map(int, input("Enter integers separated by spaces: ").split()))
target = int(input("Enter target sum: "))

result = find_subarray_with_sum(nums, target)

if result != -1:
    print(f"Subarray found from index {result[0]} to {result[1]}: {nums[result[0]:result[1]+1]}")
else:
    print("No subarray found with the given sum")


        
        
   