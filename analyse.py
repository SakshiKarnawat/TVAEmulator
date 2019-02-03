from random import *
def analyse():
 columns = 10
 rows = 10
 with open("random_num.csv", "w") as outfile:
    for x in range(rows):
        a_list = [randint(1,10) for i in range(columns)]
        values = " ".join(str(i) for i in a_list)
        print(values)
        outfile.write(values + "\n")
analyse()