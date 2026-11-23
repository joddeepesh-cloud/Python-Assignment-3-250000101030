# Question 26: Write a program to create a list of 10 numbers and display all its elements.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("List of 10 numbers:")
print(numbers)

print("Iterating over elements:")
for idx, val in enumerate(numbers):
    print(f"  Index {idx}: {val}")
