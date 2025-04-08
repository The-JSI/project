import time
from weapons import weapons_selection
from scenes.water_escape import escape_water
from scenes.dagger_path import dagger_path
from scenes.bow_path import bow_path


def swimcross(chosen_weapon):

    while True: #inner loop
        choice = input(
        "You now see a bridge, do you want to swim under it or cross it? (swim/cross) ").strip().lower()
        
        if choice == "cross":
                print("You found the gold and won!")
                is_running = False
                return False
        
        elif choice == "swim" and chosen_weapon == "dagger":
                return dagger_path()
                 
        elif choice == "swim" and chosen_weapon == "bow":
                return bow_path(chosen_weapon)

        else:
            print("You got eaten by an alligator, you die, the end!")
            is_running = False
            return False

        