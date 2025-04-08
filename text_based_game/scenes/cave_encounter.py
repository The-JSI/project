import time
from weapons import weapons_selection

def cave_encounter(chosen_weapon):
        while True:
            next_move = input("Do you want to enter the cave or rest outside? (enter/rest) ").strip().lower()
            if next_move == "enter":
                print("Inside the cave, you find a mysterious craftsman who offers to fix your bow.")
                weapons_selection[chosen_weapon].agility = 12
                print(f"Your bow has been repaired and agility is restored to {weapons_selection[chosen_weapon].agility}!")
                            #maybe can have a way to get back to a certain part in the game
                return True

            elif next_move == "rest":
                print("You rest outside. It's peaceful but nothing happens.")
                time.sleep(3)
                return False
            
            else:
                print("You wander aimlessly and end up back where you started.")