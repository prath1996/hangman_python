# coding=utf-8
"""
Hangman Python 3
"""
import os
import time
import random
import getpass
import pandas as pd

LEVEL1 = ["happy", "boycott", "worthy", "chaos", "beloved"]
LEVEL2 = ["evidence", "cynical", "ambiguous", "benevolent", "cessation"]
LEVEL3 = ["belligerent", "facetiously", "quintessential", "circumlocution",
          "extravagant"]

ALPHABETS = ['a', 'b', 'c', 'd', 'e',
             'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o',
             'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']

LIFE_LEFT = 8


def cls():
    """
    Clear Screen
    """
    os.system('clear')


def show_life():
    """
    Draw Hangman
    """
    if LIFE_LEFT == 7:
        print("   ")
        print("   ")
        print(" O ")
    elif LIFE_LEFT == 6:
        print("   ")
        print("   ")
        print(" O ")
        print(" | ")
    elif LIFE_LEFT == 5:
        print("   ")
        print("   ")
        print(" O ")
        print("/| ")
    elif LIFE_LEFT == 4:
        print("   ")
        print("   ")
        print(" O ")
        print("/|\\")
    elif LIFE_LEFT == 3:
        print("   ")
        print("   ")
        print(" O ")
        print("/|\\")
        print("/  ")
    elif LIFE_LEFT == 2:
        print("   ")
        print("   ")
        print(" O ")
        print("/|\\")
        print("/ \\")
    elif LIFE_LEFT == 1:
        print("___")
        print("   ")
        print(" O ")
        print("/|\\")
        print("/ \\")
        print("The END is Near")
    elif LIFE_LEFT == 0:
        print("___")
        print(" | ")
        print(" O ")
        print("/|\\")
        print("/ \\")


def drop():
    """
Final drop after game over
    """
    for count in range(5):
        wait(0.2)
        cls()
        print("____")
        print("  | ")
        for j in range(count):
            print("  | ")
        print(" \\O/")
        print("  | ")
        print(" / \\")


def ds1():
    """
animation
    """
    cls()
    print("____")
    print("  | ")
    for j in range(5):
        print("  | ")
    print("  O ")
    print(" /|\\")
    print(" / \\")


def ds2():
    """
animation
    """
    cls()
    print("____")
    for j in range(5):
        print("  | ")
    print("  / ")
    print("_O_")
    print(" | ")
    print("/ ) ")


def ds3():
    """
animation
    """
    cls()
    print("____")
    for j in range(5):
        print("  | ")
    print("  \\ ")
    print("  _O_")
    print("   | ")
    print("  ( \\")


def drop_dead():
    """
animation
    """
    cls()
    print("____")
    print("  | ")
    for j in range(5):
        print("  | ")
    print("  O ")
    print("  | ")
    print(" | |")
    print("Its been a long run...")


def h1():
    """
animation
    """
    cls()
    print("\n\n")
    print(" \\O/")
    print("  | ")
    print(" / \\")
    wait(0.2)


def h2():
    """
animation
    """
    cls()
    print("\n\n")
    print("  O ")
    print(" /|\\")
    print(" | |")
    wait(0.2)


def hooray():
    """
animation
    """
    for count in range(5):
        h1()
        h2()
    print("Hooray...you are alive")


def dance_of_death():
    """
animation
    """
    cls()
    print("Bye.............")
    wait(2)
    drop()
    for count in range(20):
        timer = count * 0.01
        ds1()
        wait(timer)
        ds2()
        wait(timer)
        ds1()
        wait(timer)
        ds3()
        wait(timer)
    drop_dead()


def wait(sec):
    """
sleep
    """
    time.sleep(sec)


def remove_dup(string):
    """
remove duplicate
    """
    length_string = len(string)
    new = []
    for count in range(length_string):
        new.append(string[count])

    new_len = len(new)
    for count in range(new_len):
        check = new[count]
        if check == "":
            continue
        for j in range((count + 1), new_len):
            if check == new[j]:
                new[j] = ""
    return new


def rand_word_gen(difficulty_level):
    """
random
    """
    if difficulty_level == "1":
        len_array = len(LEVEL1) - 1
        rand_int = random.randint(0, len_array)
        return LEVEL1[rand_int]
    if difficulty_level == "2":
        len_array = len(LEVEL2) - 1
        rand_int = random.randint(0, len_array)
        return LEVEL2[rand_int]
    if difficulty_level == "3":
        len_array = len(LEVEL3) - 1
        rand_int = random.randint(0, len_array)
        return LEVEL3[rand_int]


def gen_basket(word):
    """
Generates option list for given problem word
    :param word: input problem string
    :return:
    """
    avail_let = ALPHABETS
    basket = remove_dup(word)
    basket = remove_dup(''.join(basket))
    length_basket = len(basket)

    req_let = 9

    for count in range(length_basket):
        avail_let.remove(basket[count])

    avail_let_length = len(avail_let) - 1
    for count in range(req_let):
        rand_int = random.randint(0, avail_let_length)
        basket.append(avail_let[rand_int])
        del avail_let[rand_int]
        avail_let_length -= 1
    basket = random.sample(basket, len(basket))
    return basket


def show_list(arr):
    """
Display list of alphabet options left
    :param arr: Alphabet options left
    """
    length_array = len(arr)
    show = ""
    for count in range(length_array):
        show += " " + arr[count]
    print("\n")
    print(show.upper())
    show_life()
    print("\n Make a GUESS")


def create_user(new_u_name):
    """
username password for new Player
    :param new_u_name:entered username
    :return:
    """
    match_found = False
    for count in range(DF_LENGTH):
        if new_u_name == ALL_USERNAME.loc[count]:
            match_found = True
    if not match_found:
        return new_u_name
    else:
        print("Username already taken. Select new Username: ")
        new_u_name = input()
        return create_user(new_u_name)


def check_pass(index):
    """
check for password in the database
    :param index:index of row in the database
    :return:
    """
    pas = getpass.getpass(prompt="Enter password and hit enter " +
                                 "(nothing will be shown while " +
                                 "you enter password): ")
    if pas == DF.loc[index]["password"]:
        return True
    else:
        print("Wrong password\nGo back? (y/n) ")
        inp = ""
        corr_input = False
        while not corr_input:
            inp = input()
            if inp != 'Y' and inp != 'y' and inp != 'N' and inp != 'n':
                print("Entered input should be 'y' or 'n'")
            else:
                corr_input = True
        if inp == 'Y' or inp == 'y':
            login()
        else:
            check_pass(index)


def login():
    """
Login process
    """
    cls()
    print("Enter username: ")
    u_name = input()
    found = False
    for count in range(DF_LENGTH):
        if u_name == ALL_USERNAME.loc[count]:
            found = True
            check_pass(count)
    if not found:
        print("User not found!\nEnter username again: ")
        login()

cls()
print("****H A N G M A N****")
wait(1)
cls()

DF = pd.read_csv("user_data.csv")
ALL_USERNAME = DF["username"]
DF_LENGTH = ALL_USERNAME.shape[0]

print("New user? (y/n) ")
NEW_USER = ""
CORRECT_INPUT = False
while not CORRECT_INPUT:
    NEW_USER = input()
    if NEW_USER != 'Y' and NEW_USER != 'y' and NEW_USER != 'N' and NEW_USER != 'n':
        print("Entered input should be 'y' or 'n'")
    else:
        CORRECT_INPUT = True
if NEW_USER == 'Y' or NEW_USER == 'y':
    print("Enter username: ")
    NEW_USERNAME = input()
    NEW_USERNAME = create_user(NEW_USERNAME)
    P = getpass.getpass(prompt="Choose password: ")
    SIZE_DF = DF.shape[0]
    DF.loc[SIZE_DF] = [NEW_USERNAME, str(P)]
    DF.to_csv("user_data.csv", index=False)
else:
    login()

cls()
print("Choose your difficulty LEVEL - 1/2/3 ?")
LEVEL = input()
while True:
    if LEVEL != "1" and LEVEL != "2" and LEVEL != "3":
        cls()
        print("Please select difficulty from 1, 2 and 3")
        LEVEL = input()
    else:
        break

cls()
wait(1)

print("Let's begin")
wait(0.5)

print("You have 8 lives")
wait(1)

print("Good Luck")
wait(1)
print(":)")
wait(2)
cls()

PROBLEM_WORD = rand_word_gen(LEVEL)
LENGTH = len(PROBLEM_WORD)
HEADER = str(LENGTH) + " letter word\n"

BLANK_REMAINING = LENGTH
BLANKS = []
for i in range(LENGTH):
    BLANKS.append(" __")

LETTER_BASKET = gen_basket(PROBLEM_WORD)


def fill_blanks_or_draw(input_guess):
    """
Fill the BLANKS based on player's GUESS or else draw 1 more step of hangman
    :param input_guess:
    """
    global LIFE_LEFT, BLANK_REMAINING
    flag = False
    for count in range(LENGTH):
        if input_guess == PROBLEM_WORD[count]:
            BLANKS[count] = " " + input_guess.upper()
            BLANK_REMAINING -= 1
            flag = True
    if not flag:
        LIFE_LEFT -= 1
    show_life()


def check_guess(input_guess, basket):
    """
Check whether player's GUESS
    :param input_guess:
    :param basket:
    :return:
    """
    global LIFE_LEFT, BLANK_REMAINING
    for count in range(len(basket)):
        if input_guess == basket[count]:
            basket.remove(basket[count])
            fill_blanks_or_draw(input_guess)
            return basket
    cls()
    print(HEADER)
    print(''.join(BLANKS))
    show_list(basket)

    print("Select a letter only from the shown letters!")
    input_guess = input()
    return check_guess(input_guess, basket)


while LIFE_LEFT > 0 and BLANK_REMAINING > 0:
    cls()
    print(HEADER)
    print(''.join(BLANKS))
    show_list(LETTER_BASKET)

    GUESS = input()
    LETTER_BASKET = check_guess(GUESS, LETTER_BASKET)

if LIFE_LEFT == 0:
    dance_of_death()
else:
    hooray()
