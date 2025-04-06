import time
from scenes.water_escape import escape_water
from countdown import countdown
from weapons import  Weapons, weapons_selection
from intro import intro_sequence
from direction import handle_direction

name = input("Hey type your name: ")
print(f"Hello {name} welcome to the game!")

chosen_weapon = intro_sequence() #

is_running = True
while is_running:
    is_running = handle_direction()
    if is_running == False:
        break

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

                    print("You chose to get out of the water")
                    #continue here after escape_water

                elif chosen_weapon == "bow":
                    print("The water is not suitable for the bow and the string has become stiff.")
                    # Reduce the agility using chosen_weapon
                    weapons_selection[chosen_weapon].agility = 7
                    print(
                        f"The agility of the {weapons_selection[chosen_weapon].name} has been reduced to {weapons_selection[chosen_weapon].agility}.")
                    time.sleep(2)
    
                    print("You manage to drag yourself to shore, only to find a dark cave entrance.")
                
                    while True:
                        next_move = input("Do you want to enter the cave or rest outside? (enter/rest) ").strip().lower()
                        if next_move == "enter":
                            print("Inside the cave, you find a mysterious craftsman who offers to fix your bow.")
                            weapons_selection[chosen_weapon].agility = 12
                            print(f"Your bow has been repaired and agility is restored to {weapons_selection[chosen_weapon].agility}!")
                        #maybe can have a way to get back to a certain part in the game

                        elif next_move == "rest":
                            print("You rest outside. It's peaceful but nothing happens.")
                            break
                        ## this doesn't end but rather loops back to swim/cross
                        else:
                            print("You wander aimlessly and end up back where you started.")

            

                else:
                    print("You got eaten by an alligator, you die, the end!")
                    is_running = False
                    break
