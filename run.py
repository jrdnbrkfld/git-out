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
startGame = input("Would you like to start your shift? (Y/N)")
if startGame == 'n' or startGame == 'N':
    print("The boss is visually furious with you. Maybe some other time?")
elif startGame == 'y' or startGame == 'Y':
    intro()