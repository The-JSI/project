import time
from weapons import weapons_selection
from scenes.cave_encounter import cave_encounter

def bow_path(chosen_weapon):
    print("The water is not suitable for the bow and the string has become stiff.")
    
    # Reduce the agility using chosen_weapon
    weapons_selection[chosen_weapon].agility = 7
    print(f"The agility of the {weapons_selection[chosen_weapon].name} has been reduced to {weapons_selection[chosen_weapon].agility}.")
    time.sleep(2)
    
    print("You manage to drag yourself to shore, only to find a dark cave entrance.")

    while True:
        if not cave_encounter(chosen_weapon):
            exit()
