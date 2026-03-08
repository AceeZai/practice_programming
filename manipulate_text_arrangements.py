#,Prog01: Display Only Non-Duplicates
user_numbers = [float(input(f"Number {index + 1}: "))
for current_number in user_numbers:
    if user_numbers.count(current_number) == 1:
    	print(current_numbers)
    
#Prog02: Unique Entries Only (First Occurrences)
user_numbers = [float(input(f"Number {index + 1}: ")) for index in range(10)]
seen_numbers = []
for current_number in user_numbers:
    if current_number not in seen_numbers:
        print(current_number)
        seen_numbers.append(current_number)