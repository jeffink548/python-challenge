#import library 
import csv
import os

#variables needed
total_votes = 0
candidate_votes = {}
candidate_percentages = {}
winner = ""
#store csv file
election_csv = os.path.join("Resources", "election_data.csv")

#open csv file 
with open(election_csv) as csvfile:
    reader = csv.reader(csvfile)
#skip header row
    next(reader)

    #count total votes 
    for row in reader:
        total_votes += 1
    #get candidate's names
        candidate_name = row[2]
        #set new candidates vote count to 0
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0

        # add the candidate's vote count
        candidate_votes[candidate_name] += 1

#percentage of votes 
for candidate_name in candidate_votes:
    candidate_percentages[candidate_name] = round((candidate_votes[candidate_name] / total_votes) * 100, 2)

#winner of election
winner = max(candidate_votes, key=candidate_votes.get)

#print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate_name in candidate_votes:
    print(f"{candidate_name}: {candidate_percentages[candidate_name]}% ({candidate_votes[candidate_name]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
#put into text file
with open("election_results.txt", "w") as f:
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("-------------------------\n")
    for candidate_name in candidate_votes:
        f.write(f"{candidate_name}: {candidate_percentages[candidate_name]}% ({candidate_votes[candidate_name]})\n")
    f.write("-------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("-------------------------\n")
print("The analysis has been exported to election_results.txt.")
