# While loops
i = 1
while i <= 5:
    print(i)
    i = i + 1

a = 1
while a <= 10:
    print(a * '*')
    a = a + 1

# Lists
names = ["John", "Bob", "Mosh", "Sam", "Mary"]
print(names)
print(names[2])
print(names[-2])
print(names[0])
names [0] = "Jon"
print(names)
print(names[0:3])

# List Methods
numbers = [1, 2, 3, 4, 5, 6]
numbers.append(6)
print(numbers)
numbers.insert(0, -1) # you can insert anything
print(numbers)
numbers. remove(3)
print(numbers)
print(10 in numbers)
print(len(numbers))
numbers.clear()

# For Loops
numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item)

# its while loop
i = 0
while i < len(numbers):
   print(numbers[i])
   i = i + 1

# The Range Function
number = range(5)
for no in number:
    print(no)

number = range(5, 10)
for no in number:
    print(no)

number = range(5, 10, 2)
for no in number:
    print(no)

for no in range(5):
    print(no)

# Tuples: are like list used to store sequence of objects. Tuples can't be changed once created. We use parenthesis to define tuples
numbers = (1, 2, 3, 4, 4)