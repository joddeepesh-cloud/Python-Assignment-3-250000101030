# Question 03: Write a program to count vowels and consonants separately in a string.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
text = "Antigravity Python Programming"
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for ch in text:
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print(f"String: '{text}'")
print(f"Vowels Count    : {vowel_count}")
print(f"Consonants Count: {consonant_count}")
