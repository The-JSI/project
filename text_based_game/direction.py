import time
from weapons import weapons_selection
from scenes.left_path_fate import left_path_fate
from scenes.left_path_fate_2 import main

def handle_direction(chosen_weapon):
    max_dmg = 0

    while True:
        direction = input("Do you want to go left or right? (left/right) ").lower()

        if direction == "left":
           if max_dmg == 1: #checks if we went left before and if we did, executes the function. This needs to be put before max_dmg = 1 so we dont call left_path_fate
              return main(chosen_weapon) #returns true or false
           
           result = left_path_fate(chosen_weapon) #runs the first time when someone goes left
           if result == "retry":
                max_dmg = 1 # if we dont define this outside the loop as 0, max_dmg will only be limited to this scope and anything outside this loop wont know that max_dmg exists
                continue  # go back to direction
           else:
                return result  # the result in this case if not retry would have been false and the game ends

        elif direction == "right":
            return True  # Continue with the game
        else:
            print("Sorry not a valid reply, you die!")
            time.sleep(5)
            print()
            print("haha jk u not die lol")
            print("enter an actual input next time")
            print()