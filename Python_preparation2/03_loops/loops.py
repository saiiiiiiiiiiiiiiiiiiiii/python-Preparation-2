# Loop's in python 
# 1) Counting Positive Number's
# Give a List of Number's , count How many are positive 

# numbers = [1,-2,3,-4,5,6,-7,-8,9,10]
# for i in numbers:
#   if i > 0:
#     print(i)



# 2) Sum of even Numbers 
# Calculate the sum of even numbers up to given number n 

# n = int(input('Enter a Number: '))
# sum = 0
# for i in range(1, n + 1):
#   if i % 2 == 0:
#     sum = sum + i
# print(sum)


# 3) Multiplication Table Printer 
# Print the multiplication table for given number up to 10 but skip the fifth iteration


# number = int(input('Enter a Number: '))
# for i in range(1, 11):
#   if i == 5:
#     continue
#   print(f'{i} * {number} = {i * number}')


# 4) Reverse a string
# Reverse a string using loop

# string = input('Enter Your Name: ')
# Reverse_string = ""
# for i in string:
#   Reverse_string = i + Reverse_string

# print(Reverse_string)

#5) Find the first non -repeated character 
# Given a string find the first nonrepeated character 


# string = input('Enter your Name: ')
# Non_repeated_Character = ""
# for character in string:
#   print(character)
#   if string.count(character) == 1:
#     Non_repeated_Character = character

# print(f"The Non Repeated Character in {string} is {Non_repeated_Character}")





# 6) factorial of a calculator
# number = int(input("Enter a Number:"))
# factorial = 1
# for i in range(1, number + 1):
#   factorial = factorial * i

# print(factorial)



# 7) Validating Input 
# Keep asking the user for input until they enter a number between 1 to 10

# while True:
#   asking_for_number_between_1_to_10 = int(input('Enter a Number between (1 to 10): '))
#   if asking_for_number_between_1_to_10 >= 1 and asking_for_number_between_1_to_10 <= 10:
#     break




# 8) Prime Number checker 
# number = int(input("Enter a Number: "))

# if number <= 1:
#     print(f"The {number} is not a prime number.")
# else:
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(f"The {number} is a prime number.")
#     else:
#         print(f"The {number} is not a prime number.")



# 9) Problem 
# items = ["apple", "bananna","orange", "mango", "apple"]
# unique_items = set()
# for i in items:
#   if i in unique_items:
#     print('The Item is already in the list Cannot add it again')
#   else:
#     unique_items.add(i)
#     print(unique_items)

# print(type(unique_items))

# Exponantial Backoff
# implement an exponential backoff stratergy that doubles the wait time 
# between retries strating from 1 second , but restarts after 5 retries
import time
waiting_time = 1
max_tries = 5
attempts = 0
while attempts < max_tries:
  print(f"Attempts {attempts + 1} Wait_time {waiting_time}")
  waiting_time = waiting_time * 2
  attempts = attempts + 1
  time.sleep(waiting_time)