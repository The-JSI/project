import time
from weapons import weapons_selection
from scenes.left_path_fate import left_path_fate

def handle_direction(chosen_weapon):
    while True:
        direction = input("Do you want to go left or right? (left/right) ").lower()

        if direction == "left":
           result = left_path_fate(chosen_weapon)
           if result == "retry":
              continue #go back to direction
           else:
               return result # the result in this case if not retry would have been false and the game ends
     
        elif direction == "right":
            return True  # Continue with the game
        else:
            print("Sorry not a valid reply, you die!")
            time.sleep(5)
            print()
            print("haha jk u not die lol")
            print("enter an actual input next time")
            print()  