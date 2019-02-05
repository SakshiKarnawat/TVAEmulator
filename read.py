import csv

def read():
    csv_file = open("random_num.csv", "r")
    reader = csv.reader(csv_file)

    for row in reader:
        print(" ".join(row[:2]))