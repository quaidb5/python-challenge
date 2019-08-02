# PyPoll Main

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
    
    print("Election Results")
    print("-----------------------------------------------")
    print("Total Votes: " + str(votes))
    print("-----------------------------------------------")

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
    
    #print(unique_candidate)
    
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
    Total_votes = votes
    Correy_percent = Correy_votes / Total_votes
    Khan_percent = Khan_votes / Total_votes
    Li_percent = Li_votes / Total_votes
    Tooley_percent = Tooley_votes / Total_votes

    print("Correy: " + str(Correy_percent) + " (" + str(Correy_votes) + ")")
    print("Khan: " + str(Khan_percent) + " (" + str(Khan_votes) + ")")
    print("Li: " + str(Li_percent) + " (" + str(Li_votes) + ")")
    print("O'Tooley: " + str(Tooley_percent) + " (" + str(Tooley_votes) + ")")
    print("-----------------------------------------------")

    # Determining winner
    #votes_list[Correy_votes, Khan_votes, Li_votes, Tooley_votes]

    if Correy_votes > Khan_votes and Correy_votes > Li_votes and Correy_votes > Tooley_votes:
        print("Winner: Correy")
    elif Khan_votes > Correy_votes and Khan_votes > Li_votes and Khan_votes > Tooley_votes:
        print("Winner: Khan")
    elif Li_votes > Correy_votes and Li_votes > Khan_votes and Li_votes > Tooley_votes:
        print("Winner: Li")
    elif Tooley_votes > Correy_votes and Tooley_votes > Khan_votes and Tooley_votes > Li_votes:
        print("Winner Tooley")
