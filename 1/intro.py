import time
from countdown import countdown
from weapons import weapons_selection

def intro_sequence():

    while True:
        play_start = input("Do you want to play? ").strip().lower()

        if play_start in {"y", "yes"}:
            print(f"Game Start!")
            countdown(3)
            print()
            print("choose your weapon: ")
            for key, ouchies_giver in weapons_selection.items(): #weapon_name is the key and ouchies_giver is the value (name for the Weapons class)
                print(f"- {ouchies_giver.name.capitalize()} - DMG: {ouchies_giver.dmg} - Agility: {ouchies_giver.agility}") #use value.attributes to print the value of those certain attributes

            while True:
                chosen_weapon = input("enter weapon of choice: ").strip().lower()
                if chosen_weapon in weapons_selection:
                    print(f"weapon choice - {weapons_selection[chosen_weapon].name}")
                    break
                else:
                    print(f"{chosen_weapon} is not valid. Choose one from the list.")
                    continue
            print()
            return chosen_weapon
        elif play_start in {"n", "no"}:
            print("Exiting...")
            time.sleep(1)
            exit()
        else:
            print("Invalid response. Type 'y' or 'n'.")

