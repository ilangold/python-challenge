# -*- coding: UTF-8 -*-
""" Module 3 Challenge - PyPoll
    Ilan Goldstein
    2024/12/16
"""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
vote_counts = {}

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". \n", end="")
        
        # Increment the total vote count for each row
        total_votes = total_votes + 1

        # Get the candidate's name from the row
        name = row[2]

        # If the candidate is not already in the candidate list, add them
        if name not in vote_counts:
            vote_counts[name] = 1

        # Add a vote to the candidate's count
        elif name in vote_counts:
            vote_counts[name] = vote_counts[name] + 1

# Calculate percentage of votes won by each candidate
win_tally = 0
for candidate , votes in vote_counts.items():
    percentage = round(votes/total_votes*100,3)
    vote_counts[candidate] = [percentage , votes]
    # Determine which candidate won the most votes
    if vote_counts[candidate][1] > win_tally:
        win_tally = votes
        winner = candidate

# Output Header
output = ('Election Results\n'
          '-------------------------\n'
          f'Total Votes: {total_votes}\n'
          '-------------------------\n')

# Add vote counts to output
for k , v in vote_counts.items():
    output = output + (f'{k} : {v[0]}% ({v[1]})\n')

# Add winner results to output
output = output + ('-------------------------\n'
                   f'Winner: {winner}\n'
                   '-------------------------')

print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)