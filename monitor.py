from random import *
def monitor():
    n = 0
    while (n < 20):
        count = (randint(1, 10))
        if (count >= 4):
            if (count < 8):
                print (" Good value",count)
            else:
                 print(" Bad value", count)
        else:
            print(" Bad value", count)
        n+= 1
monitor()

