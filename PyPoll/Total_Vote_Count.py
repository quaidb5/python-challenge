# PyPoll Total Vote Count

import os
import csv

# grabbing the csv file for budget data
csvpath = os.path.join('election_data.csv')

#Total Months 
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    votes = 0
    for row in csvreader:
        votes = votes + 1

    print("Total Votes: " + str(votes))
    