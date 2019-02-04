from random import *
from analyse import analyse


"""
    TO DO: make the range bigger for the random number, and the 'bad' value range smaller
    so the program doesn't get killed right away
"""
def monitor():

    monitoring = True
    while (monitoring):
        count = (randint(1, 10))
        if (count >= 3):
            print("Good value: {}".format(count))
        else:
            print("Bad value: {}".format(count))
            analyse()
            monitoring = False


