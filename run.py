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
    pathOneA = input(Fore.CYAN + Style.BRIGHT + "Make your choice. (1/2/3)\n")
    if pathOneA == '1':
        path1A()
    elif pathOneA == '2':
        path1B()
    elif pathOneA == '3':
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


def path1C():
    print()
    print("""You make your way into the main halls, confused about the nature of the note.
Could this be a cruel prank the boss is playing on you?
Then you hear a guttural moan from down the hallway.
You notice a pale gaunt girl peeking staring at you from the end of the hall.
You begin to approach her, she must be a customer that accidentally got locked in. 
Her behaviour is erratic, moaning constantly like she is in agony.
She charges at you! 
Quickly, you have to do something!

Path 1: Run into the lock up to your left and trap her in.
Path 2: Charge her, you aren't scared!""")
    print()
    path1C1 = input(Fore.CYAN + Style.BRIGHT + "Make your choice. (1/2)\n")
    if path1C1 == '1':
        print()
        print("""You dart into the locker on your left, it's full of old car parts.
She slides around the corner and comes at you!
You hit her over the head with a wrench you found.
While she is dazed, you trap her in.
You call the emergency services with your mobile phone.
When they arrive, it takes 3 police officers to subdue her and put her in a secure van going to the police station.
After they had finished their inspection of the building, they found evidence suggesting the girl was the boss's daughter.
He is eventually caught days later and arrested.
The nightmare is over!""")
        win()
    elif path1C1 == '2':
        print()
        print("""You charge at her, colliding with the freak and both of you are knocked to the floor.
She quickly picks herself up.
With her razor sharp nails, she starts wildly attacking you.
Her strength is overwhelming for such a small thing.
One last violent swipe hits your neck, severing your jugular vein.
Bleeding out, the girl stands over you licking her lips.
Your body was never found.""")
        lose()
    else: 
        print()
        print(Fore.RED + Style.BRIGHT + "Error, you have not chosen a correct option.")
        print(Fore.RED + Style.BRIGHT + "Please try again.")
        path1C()


# win screen
def win():
    print(Fore.CYAN + Style.BRIGHT + """
__  __               _       ___       __
\ \/ /___  __  __   | |     / (_)___  / /
 \  / __ \/ / / /   | | /| / / / __ \/ / 
 / / /_/ / /_/ /    | |/ |/ / / / / /_/  
/_/\____/\__,_/     |__/|__/_/_/ /_(_) 
""")

# lose screen
def lose():
    print(Fore.RED + Style.BRIGHT + """
__  __               __                    __
\ \/ /___  __  __   / /   ____  ________  / /
 \  / __ \/ / / /  / /   / __ \/ ___/ _ \/ / 
 / / /_/ / /_/ /  / /___/ /_/ (__  )  __/_/  
/_/\____/\__,_/  /_____/\____/____/\___(_)   
""")

# welcome title
print(Fore.CYAN + Style.BRIGHT + """
   _______ __     ____        __ 
  / ____(_) /_   / __ \__  __/ /_
 / / __/ / __/  / / / / / / / __/
/ /_/ / / /_   / /_/ / /_/ / /_  
\____/_/\__/   \____/\__,_/\__/""")


def main():
    title()


main()
