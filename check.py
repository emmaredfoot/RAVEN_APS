import csv
import os

filename = dataset = csv.reader(open('old/APS_data_1.csv', newline=''), delimiter=',')
for row in filename:
    if float(row[1]) > 9000.0:
        print("Demand: ", row[1])
    elif float(row[1]) < 1000.0:
        print("Demand: ", row[1])
