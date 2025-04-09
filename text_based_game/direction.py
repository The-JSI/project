import time
from weapons import weapons_selection
from scenes.left_path_fate import left_path_fate

def handle_direction(chosen_weapon):
    while True:
        direction = input("Do you want to go left or right? (left/right) ").lower()

        if direction == "left":
            return left_path_fate(chosen_weapon)
        
        
        elif direction == "right":
            return True  # Continue with the game
        else:
            print("Sorry not a valid reply, you die!")
            time.sleep(5)
            print()
            print("haha jk u not die lol")
            print("enter an actual input next time")
            print()  