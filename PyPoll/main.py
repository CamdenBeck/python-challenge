# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
names = []
# votes = []
percentages = []
vote_counts = []
candidate_vote_count = 0
number_of_candidates = 0
names_and_votes = {}

# Winning Candidate and Winning Count Tracker
winning_count = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        name = row[2]

        # If the candidate is not already in the candidate list, add them
        if name not in names:
            number_of_candidates += 1
            names.append(name)
            names_and_votes[f'candidate {number_of_candidates}'] = name
            candidate_vote_count = 0
            # votes.append(candidate_vote_count)
            names_and_votes[f'{name}'] = candidate_vote_count
        
        # Add a vote to the candidate's count
        if name in names:
            candidate_vote_count = names_and_votes[f'{name}']
            candidate_vote_count += 1
            names_and_votes[f'{name}'] = candidate_vote_count

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in names:

        # Get the vote count and calculate the percentage
        vote_count = names_and_votes[f'{candidate}']
        percentage = (vote_count/total_votes)*100

        # Update the winning candidate if this one has more votes


        # Save each candidate's vote count and percentage
        vote_counts.append(vote_count)
        percentages.append(percentage)

    # Determining the winner
    max_vote_index = vote_counts.index(max(vote_counts))
    winning_candidate = names[max_vote_index]

    # Generate and print the winning candidate summary
    summary = f"""Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{names[0]}: {percentages[0]}% ({vote_counts[0]})
{names[1]}: {percentages[1]}% ({vote_counts[1]})
{names[2]}: {percentages[2]}% ({vote_counts[2]})
-------------------------
Winner: {winning_candidate}
-------------------------"""
    print(summary)

    # Save the winning candidate summary to the text file
    txt_file.write(summary)
