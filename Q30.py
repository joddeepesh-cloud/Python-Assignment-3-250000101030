# Question 30: Write a program to count the number of even and odd elements in a list.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
nums = [12, 17, 24, 33, 40, 55, 62, 71, 80]

even_count = 0
odd_count = 0

for n in nums:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("List:", nums)
print("Even numbers count:", even_count)
print("Odd numbers count :", odd_count)
