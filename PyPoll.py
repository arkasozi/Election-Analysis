# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
#OPen the election results and read the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Open the election results and read the file

# Getting the candidate name
candidate_Options = []
# Declare Dictionary for for candidate and votes
candidate_votes = {}
# Winning Candidate and winning count tracker
winning_candidate = ""
winning_count = 0
Winning_Percentage = 0
# Open election results and read the file
with open(file_to_load) as election_data:
#print the file object.
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add the total vote count  
        total_votes += 1
        # Print the candidates name from each row.
        candidate_name = row[2]
     # if the candidate does not match any existing candidate
        if candidate_name not in candidate_Options:
            #Add it to the list of candidates.
            candidate_Options.append(candidate_name)
            # Begin Tracking the candidate's votes
            candidate_votes[candidate_name] = 0
            # Increament the candidates vote by 1 each time his name appears
        candidate_votes[candidate_name] +=1

for candidates_name in candidate_votes:
    # retrieve vote count and percentage
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    print(f"{candidate_name}: {vote_percentage:.2f}% ({votes:,}) \n")
    
    # Determine winning vote count, winning percentage and candidate
    if (votes > winning_count) and ( vote_percentage > Winning_Percentage):
        # if true then set winning_count = votes and winning_percent
        # vote percentage
        winning_count = votes
        Winning_Percentage = vote_percentage
        # Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
# Print the winning candidates' results to the terminal.
winning_candidate_summary = (
    f"---------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"winning Vote Count: {winning_count:,}\n"
    f"winning Percentage: {Winning_Percentage:.1f}%\n"
    f"----------------------\n")
print(winning_candidate_summary)


# Determine winning vote count, winning percentage

        

# Print the candidate list.
print(candidate_votes)
print(candidate_Options)
# Print the total votes.
print(total_votes)


       
#Create a filename variable to a direct or indirect path to the file.

# Using the with statement open the file as a text file.
# To read and analyse the data
# Print each row in the CSV file.