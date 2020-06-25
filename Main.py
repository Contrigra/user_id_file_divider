text_name = str(input('Enter the name of a text file: '))
text = open(text_name)
text_list = text.readlines()

modulo_divider = int(input('Enter the number of files you want to have: '))
modulus = round(len(text_list) / modulo_divider)

counter = 0

file_counter = 1
divided_text = open(f"{text_name}-divided-{file_counter}.txt", "a+")

for user_id in text_list:
    divided_text.write(user_id)
    counter += 1

    if counter % modulus == 0:
        file_counter += 1
        divided_text = open(f"{text_name}-divided-{file_counter}.txt",
                            "a+")
