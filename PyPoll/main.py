import os
import csv

bank_csv = os.path.join('Resources', 'election_data.csv')

#complete list of candidates who received votes
# % of votes each candidate won
# winner of election based on popular vote

#define variables
total_votes = 0
candidates = {}
candidates_percent = {}
winner = ""
winner_count = 0

# Open and read csv
with open(bank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    #grab first row
    firstrow = next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

for key, value in candidates.items():
    candidates_percent[key] = round((value/total_votes)*100,2)

for key in candidates.keys():
    if candidates[key] > winner_count:
        winner = key
        winner_count = candidates[key]

print("Election Results")
print("-------------------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------------------")
for key, value in candidates.items():
    print(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ")")
print("-------------------------------------")
print("Winner: " + winner)
print("-------------------------------------")

new_file = open("pollresults.txt", "w")

# writing the new file
new_file.write("Election Results \n")
new_file.write("------------------------------------- \n")
new_file.write("Total Votes: " + str(total_votes) + "\n")
new_file.write("------------------------------------- \n")
for key, value in candidates.items():
    new_file.write(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ") \n")
new_file.write("------------------------------------- \n")
new_file.write("Winner: " + winner + "\n")
new_file.write("------------------------------------- \n")