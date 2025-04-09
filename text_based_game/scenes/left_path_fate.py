import time
import random
from weapons import weapons_selection

def left_path_fate(chosen_weapon):
    print("you went left...fate awaits...")
    time.sleep(3)

    if random.choice([True, False]):
        print("you fell off a cliff and died. Game Over :(")
        return False
    else:
        weapon = weapons_selection[chosen_weapon]
        weapon.dmg = weapon.max_upgradable_dmg
        print(f"✨ Miraculously, your {weapon.name} has been upgraded to its MAX DAMAGE: {weapon.dmg}!")
        time.sleep(2)
        print("You find a secret path that leads you back to the original crossroads...")
        time.sleep(2)
        return "retry"