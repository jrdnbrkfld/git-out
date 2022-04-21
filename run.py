## intro function
def intro():
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
        print("path1")
    elif firstPath == 'n' or firstPath == 'N':
        print("path2")

## title screen
print("             ################")
print("            ##              ##")
print("           ###              ###")
print("          ####    Title     ####")
print("           ###              ###")
print("            ##              ##")
print("             ################")
print()
print()
print("""You sprint off the bus.
Just your luck that it was running late on the night of your first shift.
The time is 21:56, not as early as you would have liked to have arrived.
You approach the staff entrance to the side of the building.
Your new boss is standing there, looking quite annoyed.\n""")
startGame = input("Would you like to start your shift? (Y/N)\n")
if startGame == 'n' or startGame == 'N':
    print("The boss is visually furious with you. Maybe some other time?")
elif startGame == 'y' or startGame == 'Y':
    intro()