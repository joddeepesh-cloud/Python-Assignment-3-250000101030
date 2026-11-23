# Question 50: Write a program to create two sets and perform union, intersection, difference and symmetric difference operations.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print("Set A:", set_a)
print("Set B:", set_b)

# Set operations
union_set = set_a | set_b
intersection_set = set_a & set_b
difference_set = set_a - set_b
sym_diff_set = set_a ^ set_b

print("Union (A | B)               :", union_set)
print("Intersection (A & B)        :", intersection_set)
print("Difference (A - B)          :", difference_set)
print("Symmetric Difference (A ^ B):", sym_diff_set)
