from sys import exit
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


# beginning function to start the game
def title():
    read_file("assets/story/title.txt")
    user_choice = input(Fore.CYAN + Style.BRIGHT + "Would you like to start your shift? (Y/N)\n" + Style.RESET_ALL)
    if user_choice.lower() == 'n':
        read_file("assets/story/no.txt")
    elif user_choice.lower() == 'y':
        intro()
    else:
        error()
        main()


# intro function
def intro():
    read_file("assets/story/intro.txt")
    user_choice = input(Fore.CYAN + Style.BRIGHT + "Do you want to read the note? (Y/N)\n" + Style.RESET_ALL)
    if user_choice.lower() == 'y':
        path1()
    elif user_choice.lower() == 'n':
        path2()
    else:
        error()
        intro()


# the path in which you read the note
def path1():
    read_file("assets/story/path_one.txt")
    user_choice = input(Fore.CYAN + Style.BRIGHT + "Make your choice. (1/2/3)\n" + Style.RESET_ALL)
    if user_choice == '1':
        path1A()
    elif user_choice == '2':
        path1B()
    elif user_choice == '3':
        path1C()
    else:
        error()
        path1()


# the path in which you try to exit through the door
def path1A():
    read_file("assets/story/path_one_a.txt")
    user_choice = input(Fore.CYAN + Style.BRIGHT + "Make your choice. (1/2)\n" + Style.RESET_ALL)
    if user_choice == '1':
        read_file("assets/story/path_one_a_win.txt")
        win()
    elif user_choice == '2':
        read_file("assets/story/path_one_a_lose.txt")
        lose()
    else:
        error()
        path1A()


# the path where you run back into the office and hide
def path1B():
    read_file("assets/story/path_one_b.txt")
    user_choice = input(Fore.CYAN + Style.BRIGHT + "Make your choice. (1/2)\n" + Style.RESET_ALL)
    if user_choice == '1':
        read_file("assets/story/path_one_b_lose.txt")
        lose()
    elif user_choice == '2':
        read_file("assets/story/path_one_b_win.txt")
        win()
    else:
        error()
        path1B()


# the path where you explore the main halls
def path1C():
    read_file("assets/story/path_one_c.txt")
    user_choice = input(Fore.CYAN + Style.BRIGHT + "Make your choice. (1/2)\n" + Style.RESET_ALL)
    if user_choice == '1':
        read_file("assets/story/path_one_c_win.txt")
        win()
    elif user_choice == '2':
        read_file("assets/story/path_one_c_lose.txt")
        lose()
    else:
        error()
        path1C()


# the path where you don't read the note
def path2():
    read_file("assets/story/path_two.txt")
    user_choice = input(
        Fore.CYAN + Style.BRIGHT + "Make your choice. (1/2/3)\n" + Style.RESET_ALL)
    if user_choice == '1':
        path2A()
    elif user_choice == '2':
        path2B()
    elif user_choice == '3':
        path2C()
    else:
        error()
        path2()


# the path where you do your first patrol
def path2A():
    read_file("assets/story/path_two_a.txt")
    user_choice = input(Fore.CYAN + Style.BRIGHT + "Make your choice. (1/2)\n" + Style.RESET_ALL)
    if user_choice == '1':
        read_file("assets/story/path_two_a_win.txt")
        win()
    elif user_choice == '2':
        read_file("assets/story/path_two_a_lose.txt")
        lose()
    else:
        error()
        path2A()


# the path where you boil the kettle
def path2B():
    read_file("assets/story/path_two_b.txt")
    user_choice = input(Fore.CYAN + Style.BRIGHT + "Make your choice. (1/2)\n" + Style.RESET_ALL)
    if user_choice == '1':
        read_file("assets/story/path_two_b_win.txt")
        win()
    elif user_choice == '2':
        read_file("assets/story/path_two_b_lose.txt")
        lose()
    else:
        error()
        path2B()


def path2C():
    read_file("assets/story/path_two_c.txt")
    user_choice = input(Fore.CYAN + Style.BRIGHT + "Make your choice. (1/2)\n" + Style.RESET_ALL)
    if user_choice == '1':
        read_file("assets/story/path_two_c_win.txt")
        win()
    elif user_choice == '2':
        read_file("assets/story/path_two_c_lose.txt")
        lose()
    else:
        error()
        path2C()


# win screen
def win():
    f = open("assets/ASCII/win.txt", 'r')
    print(Fore.GREEN + Style.BRIGHT + f.read())
    retry = input(Fore.CYAN + Style.BRIGHT + "Would you like to try again? Y/N\n" + Style.RESET_ALL)
    if retry.lower() == 'y':
        main()
    elif retry.lower() == 'n':
        exit()
    else:
        error()
        win()


# lose screen
def lose():
    f = open("assets/ASCII/lose.txt", 'r')
    print(Fore.RED + Style.BRIGHT + f.read())
    retry = input(Fore.CYAN + Style.BRIGHT + "Would you like to try again? Y/N\n" + Style.RESET_ALL)
    if retry.lower() == 'y':
        main()
    elif retry.lower() == 'n':
        exit()
    else:
        error()
        lose()


# welcome title
def main():
    f = open("assets/ASCII/gitout.txt", 'r')
    print(Fore.CYAN + Style.BRIGHT + f.read())
    f = open("assets/story/credits.txt", 'r')
    print(Fore.GREEN + Style.BRIGHT + f.read())
    read_file("assets/story/main.txt")
    user_choice = input(Fore.CYAN + Style.BRIGHT + "Would you like to play the game? (Y/N)\n" + Style.RESET_ALL)
    if user_choice.lower() == "y":
        title()
    elif user_choice.lower() == "n":
        read_file("assets/story/no.txt")
    else:
        error()
        main()


# error function, returns when wrong input is chosen
def error():
    f = open("assets/story/error.txt", 'r')
    print(Fore.RED + Style.BRIGHT + f.read())


# function which prints the chosen .txt file to the terminal
def read_file(current_story_file):
    with open(current_story_file) as file:
        file_text = file.read()
        print(file_text)


main()
