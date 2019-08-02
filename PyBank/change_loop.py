# using a list 
import os
import csv
import statistics

# grabbing the csv file for budget data
csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    profit_list = []
    for row in csvreader:
        profit_list.append(row[1])

    # Turns profit_list into integers
    profit_list = list(map(int, profit_list))

    change_list = []
    i = 0
    
    for i in range(len(profit_list) - 1):
        change = (profit_list[i] - (profit_list[i + 1])) * -1
        change_list.append(change)
    
print(statistics.mean(change_list))
print(max(change_list))
print(min(change_list))
