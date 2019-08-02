#Python Bank Main

import os
import csv
import statistics

# grabbing the csv file for budget data
csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # initialize months at 0 then count for each iteration
    months = 0
    profit_list = []
    month_list = []
    for row in csvreader:
        months = months + 1
        profit_list.append(row[1])
        month_list.append(row[0])

    print("Total Months: " + str(months))
    profit_list = list(map(int, profit_list))
    print("Total Profit: $" + str(sum(profit_list)))

    # Turns profit_list into integers
    profit_list = list(map(int, profit_list))

    change_list = []
    i = 0
    
    for i in range(len(profit_list) - 1):
        change = (profit_list[i] - (profit_list[i + 1])) * -1
        change_list.append(change)
    
print("Average Change: $" + str(round(statistics.mean(change_list),2)))

minpos = change_list.index(min(change_list))

maxpos = change_list.index(max(change_list))

# Need to split the month list string adding '20' and removing the '-'

max_str = str(month_list[maxpos + 1])
min_str = str(month_list[minpos + 1])
# max_str.replace('-',' 20')
final_max = max_str.replace('-','-20')
final_min = min_str.replace('-','-20')

print("Greatest Increase in Profits: " + final_max + " ($" + str((change_list[maxpos])) + ")")
print("Greatest Decrease in Profits: " + final_min + " ($" + str((change_list[minpos])) + ")")
