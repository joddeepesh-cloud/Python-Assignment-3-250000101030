# Question 20: Write a program to demonstrate string formatting using the format() method and f-strings.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
student = "Deepesh Joshi"
roll = 250000101030
score = 98.4

# 1. str.format() method
msg1 = "format() method: Student {} (Roll: {}) scored {:.2f}%".format(student, roll, score)

# 2. f-string
msg2 = f"f-string: Student {student} (Roll: {roll}) scored {score:.2f}%"

print(msg1)
print(msg2)
