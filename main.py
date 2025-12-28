#!/usr/bin/python3

def keep_asking_until_long(min_length):
    password_length = len(input("Input a password: "))

    while password_length < min_length:
        print("Not long enough!")
        password_length = len(input("Input a password: "))
                  
    print("That password is long enough!")

# def ask_until_has_number():
#     password = input("Please enter your password: ")

#     while 

#     print(password)

def ask_until_match(correct):
    password = input("Please input password: ")

    while password != correct:
        print("Your password in incorrect!")
        password = input("Please input password: ")

    print("Your password is correct! Finally!")

def count_attempts(correct):
    password = input("Input your password please: ")
    attempt_counter = 1

    while password != correct:
        attempt_counter += 1
        print("Wrong password! Try again!")
        password = input("Input your password please: ")

    print(f"Correct password! You attempted {attempt_counter} times!")



# # keep_asking_until_long TEST
# keep_asking_until_long(6)
# keep_asking_until_long(3)
# keep_asking_until_long(9)

# # ask_until_has_number TEST
# ask_until_has_number()

# # ask_until_match TEST
# ask_until_match("coffee1")
# ask_until_match("wow13")
# ask_until_match("c0d3")

# # count_attempts TEST
# count_attempts("coff33")
# count_attempts("abc123")
# count_attempts("246eight")