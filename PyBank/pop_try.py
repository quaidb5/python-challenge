
import os
import csv

# grabbing the csv file for budget data
csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    profit_list = []
    for row in csvreader:
        profit_list.append(row[1])

    

    profit_list.pop(1)

    # print(profit_list)

    Change_list = []
    months = 86
    Former = 867884
    profits_list = [int(x) for x in profit_list]

    for x in len(profits_list):
        # Former = Current
        Current = (profits_list[x])
        Change = Current - Former
        Change_list.append(Change)

