import time
import random
from weapons import weapons_selection
from scenes.cave_encounter import cave_encounter

def bow_path(chosen_weapon):
    print("The water is not suitable for the bow and the string has become stiff.")
    
    # Reduce the agility of chosen_weapon
    agility_loss = random.randint(1,7)
    weapons_selection[chosen_weapon].agility -= agility_loss #subtracts a random value between 1-7 from agility AND stores it
    
    print(f"The agility of the {weapons_selection[chosen_weapon].name} has been reduced by {agility_loss}.")
    print(f"New agility of {weapons_selection[chosen_weapon].name}: {weapons_selection[chosen_weapon].agility}")
    time.sleep(2)
    
    print("You manage to drag yourself to shore, only to find a dark cave entrance.")

    while True:
        if not cave_encounter(chosen_weapon):
            exit()
