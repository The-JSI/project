import time

def handle_direction():
    while True:
        direction = input("Do you want to go left or right? (left/right) ").lower()

        if direction == "left":
            print("You went left and fell off a cliff, game over.")
            return False  # Ends the game
        elif direction == "right":
            return True  # Continue with the game
        else:
            print("Sorry not a valid reply, you die!")
            time.sleep(5)
            print()
            print("haha jk u not die lol")
            print("enter an actual input next time")
            print()  