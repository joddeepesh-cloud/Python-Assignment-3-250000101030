# Question 05: Write a program to check whether a given string is a palindrome.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
test_str = "madam"
# Comparing string with its slice reverse
clean_str = test_str.lower().replace(" ", "")
is_palindrome = (clean_str == clean_str[::-1])

print(f"Given string: '{test_str}'")
if is_palindrome:
    print("The string IS a palindrome.")
else:
    print("The string is NOT a palindrome.")
