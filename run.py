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
    print("""You sprint to the exit.
While fumbling around trying to open the door,
you hear a guttural moan from down the hallway.
“Why won't this damn door open?!”, you scream.
You begin to hear footsteps from around the corner.
Growing louder with each stride.
Then you remember, the boss locked the door…
With seconds until whatever is approaching you appears, you must choose!

Path 1: Smash through the glass.
Path 2: Run back into the office and hide.""")
    print()
    path1A1 = input(Fore.CYAN + Style.BRIGHT + "Make your choice. (1/2)\n")
    if path1A1 == '1':
        print()
        print("""You grab the fire extinguisher nearby and smash through the glass.
While crawling through, you turn around to see a pale gaunt girl peeking around the corner at you.
She lets out a bloodcurdling scream and charges.
You narrowly avoid her razor sharp nails and manage to crawl out.
Sprinting towards the main road, you flag down the bus.
Covered in sweat, you board and begin hyperventilating in front of the driver.
“DRIVE! SHE'S BEHIND ME!”, you scream.
In a panic the driver puts his foot down, throwing you to the floor.
She stops chasing you and retreats back to the building.""")
        win()
    elif path1A1 == '2':
        print()
        print("""You dart through the door back into the office.
Quickly diving under the desk, you knock over the desk chair.
You hear the girl panting in the doorway.
She begins pacing around the room, searching for you.
Suddenly the girl sends the desk flying, revealing you curled up on the floor.
She attacks you, severing your jugular vein.
Bleeding out, the girl stands over you licking her lips.
Your body was never found.""")
        lose()
    else: 
        print()
        print(Fore.RED + Style.BRIGHT + "Error, you have not chosen a correct option.")
        print(Fore.RED + Style.BRIGHT + "Please try again.")
        path1A()


# the path where you run back into the office and hide
def path1B():
    print()
    print("""You dart underneath the desk out of sheer panic.
Could this be a cruel prank the boss is playing on you?
Then you hear a guttural moan from down the hallway.
You begin to hear footsteps coming from the hall. 
Growing louder with each stride, until you sense the presence of someone in the room with you.
Frantically scanning the area, you look for anything to use as protection.
You notice a letter opener next to you. What a coincidence!
Quickly, you have to do something!

Path 1: Stay hidden, like the coward you are.
Path 2: Attack them with the letter opener.""")
    print()
    path1B1 = input(Fore.CYAN + Style.BRIGHT + "Make your choice. (1/2)\n")
    if path1B1 == '1':
        print()
        print("""You stay under the desk, sobbing with snot dripping down your face.
The noise you are making is akin to a toddler losing their favourite toy.
Suddenly the girl sends the desk flying, revealing you curled up on the floor.
She attacks you, severing your jugular vein.
Bleeding out, the girl stands over you licking her lips.
Your body was never found.""")
        lose()
    elif path1B1 == '2':
        print()
        print("""You grab the letter opener and flip the desk as you stand up.
In a blind rage you lunge at the girl, plunging your knife into her belly.
She lets out a blood curdling scream which echoes throughout the building.
You call the emergency services with the work phone.
She is pronounced dead at the scene.
After the police had finished their inspection of the building, they found evidence suggesting the girl was the boss's daughter.
He is eventually caught days later and arrested.
The nightmare is over!""")
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
