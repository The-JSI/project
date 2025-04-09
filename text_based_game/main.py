import time
from scenes.water_escape import escape_water
from countdown import countdown
from weapons import  Weapons, weapons_selection
from intro import intro_sequence
from direction import handle_direction
from scenes.swimcross import swimcross
from scenes.dagger_path import dagger_path
from scenes.bow_path import bow_path
from scenes.cave_encounter import cave_encounter

name = input("Hey type your name: ")
print(f"Hello {name} welcome to the game!")

chosen_weapon = intro_sequence() #

is_running = True
while is_running:
    is_running = handle_direction(chosen_weapon)
    if is_running == False:
        break

    print("You Keep moving on...")
    time.sleep(3)
    
    is_running = swimcross(chosen_weapon)
    if not is_running:
        break