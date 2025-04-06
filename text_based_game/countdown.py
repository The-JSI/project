import time

def countdown(no_of_secs):
    for i in range(no_of_secs, 0, -1):
        print(i, end=' ')
        time.sleep(1)