# TASK 01
name = input("What is your name?\n") # let's the user define a name

print(f'\nHi {name}! Nice to meet you!\n' # prints the name and a greeting
      f'Welcome to the Programing Course!')


# TASK 02
reversed_word = input("Please enter a word you'd like to reverse:\n")

def reverse_string(reversed_word):
    str = ""
    for i in reversed_word:
        str = i + str
    return str


print("The original string is: " + reversed_word)
print("The reversed string is: " + reverse_string(reversed_word))


# TASK 03
num_user = int(input("Please enter a number: "))

num1 = 0
num2 = 1
temp = 0

fib_list = [num1, num2]

while temp < num_user:
    temp = num1 + num2
    if temp >= num_user:
        break
    fib_list.append(temp)
    temp = num2
    num2 = num1 + num2
    num1 = temp

print(f'The Fibionacci sequence handled according to your input is: {fib_list}')


# TASK 04
num_user = int(input("Please enter a number: "))

l1 = [0, ]

for num in range(num_user):
    if num % 3 == 0:
        continue
    l1.append(num)
print(l1)


# TASK 05
a = int(input("Please enter a number for a: "))
b = int(input("Please enter a number for b: "))
c = int(input("Please enter a number for c: "))

if a == b == c:
    print("This is an equilateral triangle in which all three sides are of equal length. \n")
elif a == b or b == c or a == c:
    print("This is an isosceles triangle in which all three sides are of equal length.\n")
elif a != b and b != c and a != c:
    print("This is an iscalene triangle in which all three sides are of equal length.\n")

while not (c < (a + b)):
    a = int(input("Please enter a number for a: "))
    b = int(input("Please enter a number for b: "))
    c = int(input("Please enter a number for c: "))
print("The triangle inequality is true.")

# TASK 06
num_user = int(input("Please enter a number: "))
assert num_user > 0 # negative Zahlen als Fehlermeldungen
print(oct(num_user))

# the following code is a first attempt of task06.a.
oct1 =""
while num_user > 0:
    #num_user / 8
    oct1 += str(num_user % 8)
    num_user = num_user // 8

print(oct1[::-1])

