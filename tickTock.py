import time

#using for loop
def tick_tock(seconds):
    tick_or_tock = 'Tick...'
    for i in range(seconds):
        print(tick_or_tock)
        time.sleep(1)
        if tick_or_tock == 'Tick...':
            tick_or_tock = "Tock..."
        else:
            tick_or_tock = 'Tick...'
tick_tock(4)

#using while loop

def tick_tock(seconds):
    tick_or_tock = 'Tick...'
    while seconds > 0:
        print(tick_or_tock)
        time.sleep(1)
        if tick_or_tock == 'Tick...':
            tick_or_tock = 'Tock...'
        else: 
            tick_or_tock = 'Tick...'
        seconds -=1
tick_tock(3)