import os


# 10.1 Learning Python
def working_with_file(file_input, num):
    with open(file_input) as file_obj:
        file_contents = file_obj.read()
        print('-------Printing 3 times-------')
        while num > 0:
            print(file_contents)
            num -= 1
        print('-------Reading entire file-------')
        print(file_contents)

    print('-------Looping over the object-------')
    lines_list = []
    with open(file_input) as file_obj:
        for line in file_obj:
            sentence = line.rstrip()
            print(sentence)
            lines_list.append(sentence)
    print('-------Storing and using outside the with block-------')
    print("Lines Stored in a list:", lines_list)
    return file_contents


file_name = 'learning_python.txt'
times_to_read = 3
contents = working_with_file(file_name, times_to_read)


# 10.2 Learning C
def replace_words(content, word):
    return content.replace('Python', word)


alternate_word = "C"
replaced_content = replace_words(contents, alternate_word)
print('-------------Replaced Python with C --------------', replaced_content)


# # 10.3 Guest
# def write_guest_user(user_name):
#     guest_file = open("guest.txt", "a")
#     guest_file.write(user_name + ' \n')
#
#
# guest = input("Please enter you name")
# write_guest_user(guest)


# # 10.4
# def guest_details(user_name):
#     print(f"Welcome {user_name}")
#     file_name_ = "Guest_book.txt"
#     if os.path.exists(file_name_):
#         append_write = 'a'  # append if already exists
#     else:
#         append_write = 'w'
#
#     guest_book = open(file_name_, append_write)
#     guest_book.write("Username: " + user_name + " is in!." + '\n')
#     guest_book.close()
#
#
# user_inp = ''
# while True:
#     user_inp = input("Please enter you name ")
#     if user_inp.lower() != 'no':
#         guest_details(user_inp)
#     else:
#         break


# # 10.5
# def programming_poll(inp):
#     file_name_poll = 'Programming_preference.txt'
#     if os.path.exists(file_name_poll):
#         append_write = 'a'  # append if already exists
#     else:
#         append_write = 'w'
#
#     preference = open(file_name_poll, append_write)
#     preference.write(inp + '\n')
#     preference.close()
#
#
# user_inp = ''
# while True:
#     preference_inp = input("Why do you like programming ")
#     if preference_inp.lower() != 'no':
#         programming_poll(preference_inp)
#     else:
#         break
#
#
# # 10.6 Credentials
# def credentials_file(name, pass_word):
#     cred = 'Credentials.txt'
#     if os.path.exists(cred):
#         with open(cred) as file_obj:
#             if name not in file_obj.read():
#                 print("User authenticated")
#             else:
#                 print("User not authenticated")
#
#
# user_name = input("Please enter your name ")
# password = input("Please enter you password ")
# credentials_file(user_name, password)

