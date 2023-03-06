import math
# -=- Python 3 Cheat Sheet -=-

# Python is a scripting language that's nice and simple to learn.
# If you wanted to print to the console, you can just write:
print('Hello, world!')

# (unlike Java, you don't need a main method, and don't need to put it in a class)

# Python is loosely typed. In other words, you don't have to be so
# explicit about what data types you're using. Let's create a variable
# to store some text, and print that out:
my_text = 'Look ma, a variable!'
print(my_text)

# String concatenation (joining strings) is also very easy:
concat_str = 'Check' + ' this' + ' out!'
print('Concatenated string: ' + concat_str)

# Tip: you actually don't need to concatenate strings yourself when using print().
# If you pass multiple things into print(), Python will concat them for you, with a space inbetween:
print('This', 'is', 'probably', 2, 'times', 'cleaner!')

# Numbers:
c = (1 + 2) * 3.5
c_as_string = str(c) # Type conversion: convert c to a string
# Note: because we're using string concatenation here, we must convert c to a string.
print('(1 + 2) * 3.5: ' + c_as_string)

# Type conversion
# It may be necessary to convert between data types. Bot messages come through
# as strings. What if you need to treat a part of the message as an integer?
my_int = int('123') # string to int
my_float = float('1.23') # string to float
my_string = str(my_int) # int to string

# Lists (arrays):
my_list = ['Something', 'Another thing']
my_list.append('Yet another')
print(my_list)

# Dictionaries (basically, maps from one thing to another):
capital_cities = {
    'Ireland': 'Dublin',
    'England': 'London',
    'Norway': 'Oslo',
    'India': 'New Delhi'
}
print('The capital of India is', capital_cities['India'])

# Loops, Conditions, and List indexing
first_thing = my_list[0] # gets the element at index 0 of the list
if first_thing == 'Something':
    print('There is Something at the start of the list (how very exciting...)')
elif first_thing == 'Impossible': # else, if...
    print('That\'s Impossible! I thought I hard coded Something?')
else:
    print('Have you been meddling with my cheat sheet??')

for thing in my_list:
    print('For loop thing:', thing)

for i in range(0, 3, 1): # range(start, stop, step)
    print('For loop with range, i =', i)

n = 2
while n >= 0:
    print('While loop "n":', n)
    n -= 1 # If you're familar with other languages, note that n-- isn't supported in python

# Functions

# A revolutionary function that takes two numbers and returns the sum
def my_sum_func(a, b):
    return a + b

sum_answer = my_sum_func(15, 7)
print('My sum function: 15 + 7 =', sum_answer)

# The Python standard library - https://docs.python.org/3/library/
# One of the biggest strenghts of Python is the extensive standard library it provides.
# Before you write a piece of functionality, you can probably save yourself some time by checking online
# if there's a standard library function that can do it out of the box!
# Here's just a few examples:
my_nums = [3, 4, 1, 7, 5]
print('Sum of my nums is:', sum(my_nums))
print('The biggest number is:', max(my_nums))
print('Sorted numbers:', sorted(my_nums))

# Headache saving tip:
# Some functions, like "sorted()" are not performed "in-place". What that means:
# When you pass a list to sorted(), a brand new list is created and returned, and the original list is left as it was.
# The sort is not performed on the original list.
print('my_nums are still unsorted!! ->', my_nums)

# -=- Advanced Topics -=-

# F strings - string formatting, if you prefer this over string concatenation.
print(f'My sum function: 15 + 7 = {sum_answer}')

# Multi variable assignment
first, second = 1, 'B'  # first == 1, second == 'B'
username, domain = 'god@heaven.com'.split('@')   # username == 'god', domain = 'heaven.com'

# List comprehensions - kind of like a compact for loop to build lists.
one_added = [n + 1 for n in my_nums]
print('New list with 1 added to each number:', one_added)

# String join() - very handy if you want to join strings without having to know how many things there are
joined_things = ', and then '.join(my_list)
print('Joined things: ', joined_things)

# Splicing
my_str = 'Cisco Jam 2023'
# start index = 0, end index = 5
print('First 5 chars:', my_str[0:5])
# Negative indexes make it start from the end. Leaving out the end index defaults to the string length.
print('Last 4 chars:', my_str[-4:])

# And if you want to get really fancy...

# Third argument: step (think 'i += 2' here)
print('Every second character: ' + my_str[::2])
# For negative step, python will start at the end and finish at the start by default.
print('Reversed:', my_str[::-1])

# "Reverse a string" is probably the most common basic interview question that is asked anywhere.
# Now you know how to do it in 6 characters of Python code!

# Python has a built in math library that implements many mathematical operations
# Such as rounding down or up
print('Pi rounded down is:', math.floor(math.pi))
print('Pi rounded up is:', math.ceil(math.pi))
# Or even the square root
print('Square root of 64 is', math.sqrt(64))