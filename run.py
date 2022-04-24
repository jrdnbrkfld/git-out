# beginning function to start the game
def title():
    print()
    print("""You sprint off the bus.
Just your luck that it was running late on the night of your first shift.
The time is 21:56, not as early as you would have liked to have arrived.
You approach the staff entrance to the side of the building.
Your new boss is standing there, looking quite worried.\n""")
    startGame = input("Would you like to start your shift? (Y/N)\n")
    if startGame == 'n' or startGame == 'N':
        print("The boss is visually furious with you. Maybe some other time?")
    elif startGame == 'y' or startGame == 'Y':
        intro()
    else:
        print()
        print("Error, you have not chosen a correct option")
        print("Please try again.")
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
    firstPath = input("Do you want to read the note? (Y/N)\n")
    if firstPath == 'y' or firstPath == 'Y':
        path1()
    elif firstPath == 'n' or firstPath == 'N':
        path2()
    else:
        print()
        print("Error, you have not chosen a correct option")
        print("Please try again.")
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
She is hungry.”""")
    print()
    pathOneA = input("""What would you like to do?
Path 1: Run to the door and try to get out.
Path 2: Hide underneath the desk.
Path 3: Make your way into the main storage halls.

Make your choice. (1/2/3)\n""")
    if pathOneA == '1':
        path1A()
    else:
        print()
        print("Error, you have not chosen a correct option")
        print("Please try again.")
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
Path 2: Run back into the office and hide.

Make your choice. (1/2)\n""")


# welcome title
print("                ################")
print("               ##              ##")
print("              ###              ###")
print("             ####    Title     ####")
print("              ###              ###")
print("               ##              ##")
print("                ################")
print()
print()


def main():
    title()


main()
