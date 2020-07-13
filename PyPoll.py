# The Data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The Percentage of votes each candidate won
#4. The total Number of votes each candidate won
#5. the winner of the election based on popular vote
# Add our dependencies
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_Save = os.path.join("Analysis", "election_analysis.txt")
# Open the election results and read the file
with open(file_to_load) as election_data:
    # To do: Read and analysze the data here
    file_reader = csv.reader(election_data)
    # read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    print(headers)
