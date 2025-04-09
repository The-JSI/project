import time
import random
from weapons import weapons_selection

def risk_greeting():

        print("So you choose to risk it all again?....")
        print()
        time.sleep(2)
        print("Very brave of you. Let's see if you truly are lucky....")
        print()
        time.sleep(3)

def eighty_percent(chosen_weapon):
        chance = random.random()
        if chance < 0.8:
            print("your greed has left you unworthy of future conquests. You fail.")
            return False
        else:
            print("Wow! you are truly one of the players of all time. Here's something for your courage")
            time.sleep(3)
            weapons_selection[chosen_weapon].agility *= 3
            print(f"The agility of {weapons_selection[chosen_weapon].name} has been upgraded to {weapons_selection[chosen_weapon].agility}")
            return True

def main(chosen_weapon): #needs chosen_weapon to pass on to eighty_percent
    risk_greeting()
    return eighty_percent(chosen_weapon) #we dont need a standalone eighty_percent() becuase it wouldnt return any value

    
if __name__ == "__main__":
    chosen = input("Enter weapon for test: ").strip().lower()
    main(chosen)

    # this is just for testing but it will not work because we are running it from the scenes folder 
    # and weapons is in the root folder so we'll need to have "from ..weapons" in the third line 
    # to run it from this file.