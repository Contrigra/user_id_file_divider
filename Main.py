"""
The program Takes a .txt file of parsed IDs as an input file
and divides it into several files
"""

# Opening the file to divide and save it's content
text_name = str(input('Enter the name of a text file: '))
text = open(text_name)
text_list = text.readlines()

# Deciding, how many files do we want
modulo_divider = int(input('Enter the number of files you want to have: '))
modulus = round(len(text_list) / modulo_divider)

# Variables for internal work
counter = 0
file_counter = 1

# Creating a file with divided text
divided_text = open(f"{text_name}-divided-{file_counter}.txt", "a+")

for user_id in text_list:
    divided_text.write(user_id)
    counter += 1

    if counter % modulus == 0:
        file_counter += 1
        divided_text = open(f"{text_name}-divided-{file_counter}.txt",
                            "a+")
