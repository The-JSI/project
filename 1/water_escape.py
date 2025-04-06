import time

def escape_water():
    while True:
        get_back_or_no = input("Do you wanna get out of the water? (y/n) ").strip().lower()
        if get_back_or_no in {"y", "yes"}:
            return True  # Player escapes the water
        elif get_back_or_no in {"n", "no"}:
            print("ok I guess.... sleep with the fishes then")
            time.sleep(2)
            return False  # Player chooses to stay
        else:
            print(f"you can't {get_back_or_no} in the water")

# we have used Return True and False because If the function directly modified is_running,
# it would tightly couple the function to your game loop.
# By returning True or False, the game loop decides what to do based on the function’s result
# Functions Should Return Data, Not Control the Game Directly