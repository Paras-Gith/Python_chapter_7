# 01 Print the following pattern
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

# rows = 5 
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end = '')
#     print('')    

# row = int(input("enter the number of rows: "))
# for i in range(1, row + 1):
#     for j in range(1, i +1):
#         print(j, end='')
#     print('')    


# 02 Write a Python program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

# num = int(input("enter the number: "))
# total = 0
# for i in range(1, num + 1):
#     total += i 
# print("sum of all numbers: ", total)    


# 03 Print multiplication table of a given number

# num = int(input("enter the number: "))
# for i in range(1, 11):
#     print(num * i)


# 04 Write a Python program to display only those numbers from a list that satisfy the following conditions

# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the following number
# If the number is greater than 500, then stop the loop

# numbers = [12, 75, 150, 180, 145, 525, 50]

# for num in numbers:
#     if num > 150:
#             continue
#     if num > 500:
#             break
#     if num % 5 == 0: 
#           print(num)        



# 05 Write a Python program to print the reverse number pattern using a for loop.
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

# row = 5
# for i in range(row, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end ='')
#     print('')    


# 06 Print list in reverse order using a loop

# numbers = [10, 20, 30, 40, 50]
# for value in reversed(numbers):
#     print(value)


# 07 Display numbers from -10 to -1 using for loop

# for num in range(-10, 0):
#     print(num)


# 08 Display a message “Done” after the successful execution of the for loop

# num = int(input("enter the number:"))
# for i in range(num + 1):
#     print(i)
# print("done")    


# 09 Print all prime numbers within a range\

# start = int(input("enter the number: "))
# end = int(input("enter the number: "))

# if start < 2 or end < 2:
#     print("not applicable")

# else:
#     for num in range(start, end+1):
#             is_prime = True
#             if num < 2 :
#                  is_prime = False
#             else:
#                   for i in range(2, int(num**0.5)+1):
#                        if num % i == 0 :
#                             is_prime = False
#                             break
#             if is_prime:
#                  print(num)          


# 10 Display Fibonacci series up to 10 terms

# n1= int(input("enter the number: "))
# n2 = int(input("enter the number: "))
# n_term = 10

# if n_term < 0:
#     print("enter the positive integer")
# elif n_term == 1:
#     print(n1)
# else:
#     print(n1, n2, end = " ")
#     for i in range(2, n_term):
#         nth = n1 + n2
#         print(nth, end = " ")
#         n1 = n2
#         n2 = nth



# n1 = int(input("enter the number: "))
# n2 = int(input("enter the number: "))

# n_term = int(input("enter the number of turns: "))

# if n_term < 0 :
#     print("enter the positive intger")
# elif n_term == 1 :
#     print("n1")
# else:
#     print(n1, n2, end = " ")
#     for i in range(2, n_term):
#         nth =n1 + n2 
#         print(nth, end =" ")
#         n1 = n2 
#         n2 =  nth        

