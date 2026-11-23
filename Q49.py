# Question 49: Write a program to demonstrate tuple immutability and create a modified tuple using concatenation.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
original_tuple = (10, 20, 30)
print("Original Tuple:", original_tuple)

print("\n--- Demonstrating Tuple Immutability ---")
try:
    # Tuples are immutable: assigning an item raises a TypeError at runtime
    original_tuple[0] = 99
except TypeError as e:
    print("Caught TypeError as expected:", e)
    print("Explanation: Tuples cannot be modified in place once created.")

# Creating a new modified tuple using slicing and concatenation
modified_tuple = (99,) + original_tuple[1:]
print("\n--- Creating Modified Tuple via Concatenation ---")
print("Modified Tuple:", modified_tuple)
