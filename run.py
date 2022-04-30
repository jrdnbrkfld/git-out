from sys import exit
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)


# beginning function to start the game
def title():
    print()
    f = open("assets/story/title.txt", 'r')
    print(f.read())
    print()
    startGame = input(Fore.CYAN + Style.BRIGHT + "Would you like to start your shift? (Y/N)\n")
    if startGame == 'n' or startGame == 'N':
        print(Style.RESET_ALL + "The boss is visually furious with you. Maybe some other time...")
    elif startGame == 'y' or startGame == 'Y':
        intro()
    else:
        print()
        print(Fore.RED + Style.BRIGHT + "Error, you have not chosen a correct option.")
        print(Fore.RED + Style.BRIGHT + "Please try again.")
        main()


# intro function
def intro():
    print()
    f = open("assets/story/intro.txt", 'r')
    print(f.read())
    print()
    firstPath = input(Fore.CYAN + Style.BRIGHT + "Do you want to read the note? (Y/N)\n")
    if firstPath == 'y' or firstPath == 'Y':
        path1()
    elif firstPath == 'n' or firstPath == 'N':
        path2()
    else:
        print()
        print(Fore.RED + Style.BRIGHT + "Error, you have not chosen a correct option.")
        print(Fore.RED + Style.BRIGHT + "Please try again.")
        intro()


# the path in which you read the note
def path1():
    print()
    f = open("assets/story/path_one.txt", 'r')
    print(f.read())
    print()
    path_one_a = input(Fore.CYAN + Style.BRIGHT + "Make your choice. (1/2/3)\n")
    if path_one_a == '1':
        path1A()
    elif path_one_a == '2':
        path1B()
    elif path_one_a == '3':
        path1C()
    else:
        print()
        print(Fore.RED + Style.BRIGHT + "Error, you have not chosen a correct option.")
        print(Fore.RED + Style.BRIGHT + "Please try again.")
        path1()


# the path in which you try to exit through the door
def path1A():
    print()
    f = open("assets/story/path_one_a.txt", 'r')
    print(f.read())
    print()
    path1A1 = input(Fore.CYAN + Style.BRIGHT + "Make your choice. (1/2)\n")
    if path1A1 == '1':
        print()
        f = open("assets/story/path_one_a_win.txt", 'r')
        print(f.read())
        win()
    elif path1A1 == '2':
        print()
        f = open("assets/story/path_one_a_lose.txt", 'r')
        print(f.read())
        lose()
    else:
        print()
        print(Fore.RED + Style.BRIGHT + "Error, you have not chosen a correct option.")
        print(Fore.RED + Style.BRIGHT + "Please try again.")
        path1A()


# the path where you run back into the office and hide
def path1B():
    print()
    f = open("assets/story/path_one_b.txt", 'r')
    print(f.read())
    print()
    path1B1 = input(Fore.CYAN + Style.BRIGHT + "Make your choice. (1/2)\n")
    if path1B1 == '1':
        print()
        f = open("assets/story/path_one_b_lose.txt", 'r')
        print(f.read())
        lose()
    elif path1B1 == '2':
        print()
        f = open("assets/story/path_one_b_win.txt", 'r')
        print(f.read())
        win()
    else:
        print()
        print(Fore.RED + Style.BRIGHT + "Error, you have not chosen a correct option.")
        print(Fore.RED + Style.BRIGHT + "Please try again.")
        path1B()


# the path where you explore the main halls
def path1C():
    print()
    f = open("assets/story/path_one_c.txt", 'r')
    print(f.read())
    print()
    path1C1 = input(Fore.CYAN + Style.BRIGHT + "Make your choice. (1/2)\n")
    if path1C1 == '1':
        print()
        f = open("assets/story/path_one_c_win.txt", 'r')
        print(f.read())
        win()
    elif path1C1 == '2':
        print()
        f = open("assets/story/path_one_c_lose.txt", 'r')
        print(f.read())
        lose()
    else:
        print()
        print(Fore.RED + Style.BRIGHT + "Error, you have not chosen a correct option.")
        print(Fore.RED + Style.BRIGHT + "Please try again.")
        path1C()


# the path where you don't read the note
def path2():
    print()
    f = open("assets/story/path_two.txt", 'r')
    print(f.read())
    print()
    path_two_a = input(Fore.CYAN + Style.BRIGHT + "Make your choice. (1/2/3)\n")
    if path_two_a == '1':
        path2A()
    elif path_two_a == '2':
        path2B()
    elif path_two_a == '3':
        print("path2C")
    else:
        print()
        print(Fore.RED + Style.BRIGHT + "Error, you have not chosen a correct option.")
        print(Fore.RED + Style.BRIGHT + "Please try again.")
        path2()


# the path where you do your first patrol
def path2A():
    print()
    f = open("assets/story/path_two_a.txt", 'r')
    print(f.read())
    print()
    path2A1 = input(Fore.CYAN + Style.BRIGHT + "Make your choice. (1/2)\n")
    if path2A1 == '1':
        print()
        f = open("assets/story/path_two_a_win.txt", 'r')
        print(f.read())
        win()
    elif path2A1 == '2':
        print()
        f = open("assets/story/path_two_a_lose.txt", 'r')
        print(f.read())
        lose()
    else:
        print()
        print(Fore.RED + Style.BRIGHT + "Error, you have not chosen a correct option.")
        print(Fore.RED + Style.BRIGHT + "Please try again.")
        path2A()


# the path where you boil the kettle
def path2B():
    print()
    f = open("assets/story/path_two_b.txt", 'r')
    print(f.read())
    print()
    path2B1 = input(Fore.CYAN + Style.BRIGHT + "Make your choice. (1/2)\n")
    if path2B1 == '1':
        print()
        f = open("assets/story/path_two_a_win.txt", 'r')
        print(f.read())
        win()
    elif path2B1 == '2':
        print()
        lose()
    else:
        print()
        print(Fore.RED + Style.BRIGHT + "Error, you have not chosen a correct option.")
        print(Fore.RED + Style.BRIGHT + "Please try again.")
        path2B()

# win screen
def win():
    print(Fore.GREEN + Style.BRIGHT + """
__  __               _       ___       __
\ \/ /___  __  __   | |     / (_)___  / /
 \  / __ \/ / / /   | | /| / / / __ \/ / 
 / / /_/ / /_/ /    | |/ |/ / / / / /_/  
/_/\____/\__,_/     |__/|__/_/_/ /_(_) 
""")
    retry = input(Fore.CYAN + Style.BRIGHT + "Would you like to try again? Y/N\n")
    if retry == 'y' or retry == 'Y':
        main()
    elif retry == 'n' or retry == 'N':
        exit()
    else:
        print()
        print(Fore.RED + Style.BRIGHT + "Error, you have not chosen a correct option.")
        print(Fore.RED + Style.BRIGHT + "Please try again.")
        win()


# lose screen
def lose():
    print(Fore.RED + Style.BRIGHT + """
__  __               __                    __
\ \/ /___  __  __   / /   ____  ________  / /
 \  / __ \/ / / /  / /   / __ \/ ___/ _ \/ / 
 / / /_/ / /_/ /  / /___/ /_/ (__  )  __/_/  
/_/\____/\__,_/  /_____/\____/____/\___(_)   
""")
    retry = input(Fore.CYAN + Style.BRIGHT + "Would you like to try again? Y/N\n")
    if retry == 'y' or retry == 'Y':
        main()
    elif retry == 'n' or retry == 'N':
        exit()
    else:
        print()
        print(Fore.RED + Style.BRIGHT + "Error, you have not chosen a correct option.")
        print(Fore.RED + Style.BRIGHT + "Please try again.")
        lose()


# welcome title
def main():
    print(Fore.CYAN + Style.BRIGHT + """
   _______ __     ____        __ 
  / ____(_) /_   / __ \__  __/ /_
 / / __/ / __/  / / / / / / / __/
/ /_/ / / /_   / /_/ / /_/ / /_  
\____/_/\__/   \____/\__,_/\__/""")
    title()


main()
