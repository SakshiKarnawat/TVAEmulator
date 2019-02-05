from random import *
import csv

"""
    TO DO: this function should call the DBMF functions that I provided for you in the email. If you need help
    figuring out how the data needs to be formatted in order to call the DBMF functions correctly, let me know.

    The following is what should happen with this analyse function:
    1. Read in CSV file, this will contain latency values in one column (this is all you will need, just use a random csv file for now)
    2. Feed these values into the DBMP functions so it can do it's magic
"""
def analyse():

 columns = 10
 rows = 10
 with open("random_num.csv", "w") as csv_file:
    #csv_reader = csv.DictReader(csv_file)
    for x in range(rows):
        a_list = [randint(1,9) for i in range(columns)]
        values = 'Latency values: ' + " ".join(str(i) for i in a_list)
        print(values)

        csv_file.write(values + "\n")

