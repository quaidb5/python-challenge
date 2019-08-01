# Determining the candidates names

import os
import csv
from collections import Counter

# grabbing the csv file for budget data
csvpath = os.path.join('election_data.csv')

# Candidate Names 
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    candidates_list = []
    for row in csvreader:
        candidate = row[2]
        candidates_list.append(candidate)

    unique_candidate = set(candidates_list)
    
    print(unique_candidate)