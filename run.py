import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)


# beginning function to start the game
def title():
    print()
    print("""You sprint off the bus.
Just your luck that it was running late on the night of your first shift.
The time is 21:56, not as early as you would have liked to have arrived.
You approach the staff entrance to the side of the building.
Your new boss is standing there, looking quite worried.\n""")
    startGame = input(Fore.CYAN + Style.BRIGHT + "Would you like to start your shift? (Y/N)\n")
    if startGame == 'n' or startGame == 'N':
        print("The boss is visually furious with you. Maybe some other time...")
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
    print("""Ten minutes was all the time you needed for the training.
It was a simple job on paper.
Patrol the building.
Keep an eye on the locks & fire escapes.
On his way out, the boss places a handwritten note in your hand.
'Please make sure you read this when I`ve left', he says.
He exits the door, locking it and making his way to his car.""")
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
    print("""You peel the note open.
"Why is there blood on it?", you ask yourself.
The writing is barely legible, but you persevere.
Your face goes pale, your hairs stick up on your arms.
The note reads…
“I'm so sorry, I had no other choice.
She is hungry.”
What would you like to do?

Path 1: Run to the door and try to get out.
Path 2: Hide underneath the desk.
Path 3: Make your way into the main storage halls.""")
    print()
    pathOneA = input(Fore.CYAN + Style.BRIGHT + "Make your choice. (1/2/3)\n")
    if pathOneA == '1':
        path1A()
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
    pathOneAOne = input(Fore.CYAN + Style.BRIGHT + "Make your choice. (1/2)\n")
    if pathOneAOne == '1':
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
    elif pathOneAOne == '2':
        print()
        print("""You dart through the door back into the office.
Quickly diving under the desk, you knock over the desk chair.
You hear the girl panting in the doorway.
She begins pacing around the room, searching for you.
Suddenly the girl sends the desk flying, revealing you curled up on the floor.
She attacks you, severing your jugular vein.
Bleeding out, the girl stood over you licking her lips.
Your body was never found.""")
        lose()
    else: 
        print()
        print(Fore.RED + Style.BRIGHT + "Error, you have not chosen a correct option.")
        print(Fore.RED + Style.BRIGHT + "Please try again.")
        path1A()

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
