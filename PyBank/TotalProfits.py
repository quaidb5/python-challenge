
# Netting Profit/Loss

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
    
    # iterate for total profit
    # profits = 0
    # for row in csvreader:
    #     profits = profits + int(row[1])

    # print("$" + str(profits))
    # store profits in a list
    profit_list = []
    for row in csvreader:
        profit_list.append(row[1])

    #print(max(profit_list))
    
    #print(min(profit_list))


# with open(csvpath, newline='') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=',')
#     csv_header = next(csvreader)
#     print(f"CSV Header: {csv_header}")

#     profit_list = []
#     for row in csvreader:
#         profit_list.append(row[1])
#     print(profit_list)