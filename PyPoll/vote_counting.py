 # Voting Percentage for each Candidate

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
    
    # Initialize counters
    Khan_votes = 0
    Correy_votes = 0
    Li_votes = 0
    Tooley_votes = 0

    # Counting votes by candidate
    for row in csvreader:
        if row[2] == "Correy":
            Correy_votes = Correy_votes + 1
        if row[2] == "Khan":
            Khan_votes = Khan_votes + 1
        if row[2] == "Li":
            Li_votes = Li_votes + 1
        if row[2] == "O'Tooley":
            Tooley_votes = Tooley_votes + 1

    # Converting vote amount into percentages
    Total_votes = 3521001
    Correy_percent = Correy_votes / Total_votes
    Khan_percent = Khan_votes / Total_votes
    Li_percent = Li_votes / Total_votes
    Tooley_percent = Tooley_votes / Total_votes

    print("Correy: " + str(Correy_percent) + " (" + str(Correy_votes) + ")")
    print("Khan: " + str(Khan_percent) + " (" + str(Khan_votes) + ")")
    print("Li: " + str(Li_percent) + " (" + str(Li_votes) + ")")
    print("O'Tooley: " + str(Tooley_percent) + " (" + str(Tooley_votes) + ")")

    