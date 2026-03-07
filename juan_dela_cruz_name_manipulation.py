#Program #1
#Ask for name with leading spaces. ex; ____ Acee Zai Mendez
full_name = input("Enter your full name: ")
#Use lstrip.(), this function removes spaces in the beginning of a string
clean_name = full_name.lstrip()
#Print clean_name
print(clean_name)

#Program #2
#Ask for numbers 0-1000
num_input = int(input("Enter a number (0-1000): "))
num_sixdigit = f"{num_input:06}"
print(num_sixdigit)

#Program #3
#Input mixed lower and uppercase names
full_name = input("Please enter your full name: ")
#Use upper() function
uppercase_name = full_name.upper()
print(uppercase_name)

#Program #4
#Use the code from upper but use lower() function
full_name = input("Please enter your full name: ")
lowercase_name = full_name.lower()
print(lowercase_name)

#Program #5
#A program to convert incorrect casing to proper casing
incorrect_casing = input("Please enter your name with incorrect casing: ")
#Use title() function (Converts the first character of every word in a string to uppercase and the remaining characters to lowercase, returning a new, title-cased string.)
proper_casing = incorrect_casing.title()
print(proper_casing)

