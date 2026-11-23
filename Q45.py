# Question 45: Write a program to demonstrate the use of append(), extend() and insert() methods.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
numbers = [10, 20]
print("Initial:", numbers)

# append() adds single element to end
numbers.append(30)
print("After append(30):", numbers)

# extend() adds multiple elements from iterable
numbers.extend([40, 50])
print("After extend([40, 50]):", numbers)

# insert() adds element at specified index
numbers.insert(1, 15)
print("After insert(1, 15):", numbers)
