#Program #1
#Ask for name with leading spaces. ex; ____ Acee Zai Mendez
full_name = input("Enter your fullname: ")
#Use lstrip.(), this function removes spaces in the beginning of a string
clean_name = full_name.lstrip()
#Print clean_name
print(clean_name)

#Program #2
#Ask for numbers 0-1000
num_input = int(input("Enter a number (0-1000): "))
# Add zeros to make it a 6 digit format
print ("000", + num_input)

