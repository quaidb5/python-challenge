# date of biggest profit/biggest loss

import os
import csv


# grabbing the csv file for budget data
csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    month_list = []
    profit_list = []
    for row in csvreader:
        profit_list.append(row[1])
        month_list.append(row[0])

    
    # Turns profit_list into integers
    profit_list = list(map(int, profit_list))

    change_list = []
    i = 0
    
    for i in range(len(profit_list) - 1):
        change = (profit_list[i] - (profit_list[i + 1])) * -1
        change_list.append(change)


    # i = 1
    # for i in range(len(change_list)):
    #     if change_list[i] > change_list[i - 1]:
    #         high_change = change_list[i]

    minpos = change_list.index(min(change_list))

    maxpos = change_list.index(max(change_list))

# Need to split the month list string adding '20' and removing the '-'

print(str(month_list[maxpos + 1]) + " $" + str((change_list[maxpos])))
print(str(month_list[minpos + 1]) + " $" + str((change_list[minpos])))
