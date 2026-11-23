# Question 32: Write a program to append five elements to an existing list.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
numbers = [1, 2, 3]
print("Initial list:", numbers)

elements_to_append = [4, 5, 6, 7, 8]
for el in elements_to_append:
    numbers.append(el)

print("After appending 5 elements:", numbers)
