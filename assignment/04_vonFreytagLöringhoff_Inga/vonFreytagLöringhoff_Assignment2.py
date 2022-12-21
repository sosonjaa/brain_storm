# Task 01 – String Length

# Write a program that reads in a string and prints the length of the input string.
# Do not use any built-in functions of Python, such as len().
# For example, if the input is “Computer Science”, the output should be length: 16.

word = input("Please enter a word: ") # user puts an input
count = 0 #

for x in word:
    count += 1

print(f'Length: {count}.')


# Task 02 – Largest List Element

# Write a program that generates a list of 10 random integers between 1 and 100 and then finds and prints the largest element in the list.
# Do not use the built-in function max().
# For example, if the input is [23,3,42,29,12,15,8,4,37,34], the output should be the largest element: 42.

# Hint: Check out the module random.


from random import *

num_count = 0

num_list = []


while num_count != 10:
    num_list.append(randint(1, 100))
    num_count += 1


print(num_list)

max = num_list[0] # we assume that the first item of our list is the biggest number
# if our assumption is wrong, we need to iterate over this list, need to loop through it and get each item to
# compare it to max, if it's greater than max, then we need to reset max to that number

for number in num_list:
    if number > max:
        max = number

print(max)



#Task 03 – Character Frequency

#Write a program that:

    #Reads in a string and removes any spaces from the string
    #Counts how often individual characters occur in the string
    #Stores the information on character occurrence frequency in a dictionary
    #Prints the dictionary.

#For example, if the input is “santa claus”, the output should be: {'s': 2, 'a': 3, 'n': 1, 't': 1, 'c': 1, 'l': 1, 'u': 1}.


from collections import  Counter




text = input("Please write a sentence: ")


def remove(text):
    return text.replace(" ", "")

no_spaces = remove(text)


indi_characters = set()


for x in no_spaces:
    indi_characters.add(x)

counter = dict(Counter(no_spaces))
print(counter)


# Task 04 – Sorted List of Tuples

#Write a program that:

    #Generates a list of 10 tuples, each tuple consisting of 3 random integers between 1 and 100
    #Sorts the list of tuples in increasing order of the third element in each tuple
    #Prints the sorted list of tuples

#For example, if the generated input list is: [(56, 77, 69), (43, 30, 38), (2, 77, 101), (93, 57, 4), (74, 21, 77), (39, 68, 68), (65, 53, 96), (16, 29, 88), (88, 70, 38)]
#The output should be: [(93, 57, 4), (43, 30, 38), (88, 70, 38), (39, 68, 68), (56, 77, 69), (74, 21, 77), (16, 29, 88), (65, 53, 96), (2, 77, 101)]

#Hint: You are allowed and encouraged to use built-in functions, such as sorted(), for this task.

from random import *
from operator import itemgetter


tup_list = list(tuple((randint(1, 100),randint(1, 100),randint(1, 100)) for n in range(1, 11)))
print(tup_list)

sorted_tup = sorted(tup_list, key = itemgetter(-1))
print(f'\nThe sorted list of tuples is: \n{sorted_tup}')



# Task 05 – Check Brackets

#Write a program that reads in a string, which is supposed to be a mathematical expression.
# Focus on brackets only and check whether left and right brackets are composed correctly.
# Ignore all other characters (i.e. you don’t have to check correctness of operators and operands).

# Examples of correct input:

    #3*(2+5)
    #((()())())
    #(3+)(((4)))
    #Empty string

#Examples of incorrect input:

    #(3*(2+5)
    #((()())(())
    #(3+)((4)))
    #())(()


user_input = input(str("Please enter your mathematical expression: "))



for x in user_input:
    x = user_input.count("(")

for y in user_input:
    y = user_input.count(")")

if x == y:
    print("You're mathematical expression is correct!")
else:
    print("Please check if you are missing a bracket somewhere.")



#Task 06 – Check Brackets II

#Extend previous program, so it can handle also square and curly brackets.
# Note that expressions in brackets cannot overlap. So, expression {[()()]([[]])}{} is correct, but expression ([)] is not.



user_input = input(str("Please enter your mathematical expression: "))

for special_character in ["0","1","2","3","4","5","6","7","8","9","+","-","*","/", " "]:
    user_input.replace(special_character, "")

while True:
    new_string = user_input
    user_input = user_input.replace("()", "")
    user_input = user_input.replace("[]", "")
    user_input = user_input.replace("{}", "")
    if user_input == "":
        print("Korrekt")
        break
    if new_string == user_input:
        print("String is falsch.")
        break



#Task 07 – Queue

#Write a program that simulates a queue.
# It will read strings from the input.
# Consider these inputs as names of people coming to the end of a queue.
# Whenever “next” is given as input, the program will print out the name on the turn.
# The program finishes as soon as the queue is empty.

queue = ["John", "Mary", "Wobbles", "Sacajawea"]


# how to use a while loop until list is empty:
while len(queue) > 0:

    user_input = input(str('Please provide an input (your name or "next"): \n'))

    if user_input == "next":
        print(f"{queue[0]}, it's your turn!")
        queue.pop(0)
    else:
        queue.append(user_input)
        print(f"Hey there {user_input}, please wait in the queue. Your current position is: {len(queue)}. ")

print("\nWe are closed for today, thanks for coming in, byebye!")





def to_the_power_function(x,n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x * to_the_power_function(x, n - 1)




#Task 09 – Unlimited Power II

#Using function for factorial and function x**n from previous task,
# write a program that reads value of x and prints approximate value of e**x.
# Use this formula (Taylor series) for calculation
#e**x = 1 + x + (x**2 / 2!) + (x**3 / 3!) + ... + (x**n / n!)

#To get precise value of e**x, the series would have to be infinite.
# Suppose that there is some required accuracy,
# so the calculation finishes as soon as the value of the next element is smaller than given threshold (e.g., 0.000001).

from math import factorial

from Task08 import to_the_power_function


def taylor(x):
    n = 0
    result_dividend = 1
    result_taylor = 1

    while result_dividend >= 0.000001:
        n += 1
        result_dividend = to_the_power_function(x,n)/factorial(n)
        result_taylor += result_dividend
    return result_taylor

