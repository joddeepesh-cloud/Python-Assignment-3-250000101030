# Question 48: Write a program to demonstrate tuple concatenation, repetition and slicing.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Concatenation
t_concat = t1 + t2
# Repetition
t_repeat = t1 * 3
# Slicing
t_slice = t_concat[1:5]

print("t1:", t1)
print("t2:", t2)
print("Concatenation (t1 + t2):", t_concat)
print("Repetition (t1 * 3)    :", t_repeat)
print("Slicing (t_concat[1:5]):", t_slice)
