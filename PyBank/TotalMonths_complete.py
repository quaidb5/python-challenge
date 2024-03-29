#Python Bank Main

import os
import csv

# grabbing the csv file for budget data
csvpath = os.path.join('budget_data.csv')

#Total Months 
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # initialize months at 0 then count for each iteration
    months = 0
    for row in csvreader:
        months = months + 1

    print("Total Months: " + str(months))

# Total Profits
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    # iterate for total profit
    profits = 0
    for row in csvreader:
        profits = profits + int(row[1])

    print("Total Profits: $" + str(profits))