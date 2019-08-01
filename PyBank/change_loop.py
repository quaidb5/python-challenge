
import os
import csv

# grabbing the csv file for budget data
csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    profit_list = []
    for row in csvreader:
        profit_list.append(row[1])
    # print(profit_list)
    profit_list = [int(i) for i in profit_list]
   
# with open(csvpath, newline='') as csvfile:

#     csvreader = csv.reader(csvfile, delimiter=',')
#     csv_header = next(csvreader)

    change_list = []
    for i in range(0, len(profit_list)):
        change = profit_list[i] - (profit_list[i] + 1)
        change_list.append(change)

print(change_list)
