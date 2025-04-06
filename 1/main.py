import time
from water_escape import escape_water
from countdown import countdown
from weapons import  Weapons, weapons_selection
from intro import intro_sequence

name = input("Hey type your name: ")
print(f"Hello {name} welcome to the game!")

chosen_weapon = intro_sequence() #

is_running = True
while is_running: #controls the outer loop

    direction = input("Do you want to go left or right? (left/right) ").lower()
    if direction == "left":
        print("You went left and fell off a cliff, game over.")
        break

    elif direction == "right":
        while True: #inner loop
            choice = input(
            "You now see a bridge, do you want to swim under it or cross it? (swim/cross) ").strip().lower()

            if choice == "cross":
                print()
                print("oh noes there are enemies. Prepare Yourself")
                countdown(5)
                pass #work here later

                print("You found the gold and won!")
                is_running = False
                break #without break, we would continue running this inner while loop even if the outer is_running = False

            elif choice == "swim":
                if chosen_weapon == "dagger":
                    print("There was an alligator in the water. However, the dagger was swift enough to have defeat it.")
                    time.sleep(3)
                    print()
                    print("You live. Now get back")
                    time.sleep(2)

                    if not escape_water():
                        is_running = False
                        break

                elif chosen_weapon == "bow":
                    print("The water is not suitable for the bow and the string has become stiff.")
                    # Reduce the agility using chosen_weapon
                    weapons_selection[chosen_weapon].agility = 7
                    print(
                        f"The agility of the {weapons_selection[chosen_weapon].name} has been reduced to {weapons_selection[chosen_weapon].agility}.")

                else:
                    print("You got eaten by an alligator, you die, the end!")
                    is_running = False
                    break

    else:
        print("Sorry not a valid reply, you die!")
        time.sleep(5)
        print()
        print("haha jk u not die lol")
        print("enter an actual input next time")
        print()
