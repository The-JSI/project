import time
from scenes.water_escape import escape_water

def dagger_path():

    print("There was an alligator in the water. However, the dagger was swift enough to defeat it.")
    time.sleep(2)
    print("You live. Now get back.")

    if not escape_water():
        return False

    else:
        print("You chose to get out of the water safely.")
        return True