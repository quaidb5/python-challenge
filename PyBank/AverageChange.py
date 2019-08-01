# Average Change in Profit/Loss over the whole period

import os
import csv

# grabbing the csv file for budget data
csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    Change_list = []
    months = 86
    Current = 0
    

    for row in csvreader:
        # Former = Current
        Current = int(row[1])
        Change = Current - Former
        Change_list.append(Change)

    #Overall_Change = Overall_Change - 867884
    #Average_Change = Overall_Change / months

    # For row in csvreader:
    #     Former = Current
    #     Current = int(row[1])
    #     Change = Current - Former
    #     Change_list.append(change)

    print(Change_list)
      