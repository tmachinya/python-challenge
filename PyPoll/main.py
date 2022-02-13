import os
import csv

# path to the csvfile
csvpath = os.path.join('election_data.csv')

# initializing the variables
pollData = {}
allVotes = 0
with open(csvpath, 'r') as csvfile:
    data = csv.reader(csvfile)
    next(data, None)

    for row in data:
        allVotes += 1
        if row[2] in pollData.keys():
            pollData[row[2]] = pollData[row[2]] + 1
        else:
            pollData[row[2]] = 1

candidates = []
totalVotes = []
# Total Number of votes
for key, value in pollData.items():
    candidates.append(key)
    totalVotes.append(value)

# Percentage of votes
percentage_votes = []
for n in totalVotes:
    percentage_votes.append(n / allVotes * 100)

# Finding the winner
clean_data = list(zip(candidates, totalVotes, percentage_votes))

winner_list = []
for name in clean_data:
    if max(totalVotes) == name[1]:
        winner_list.append(name[0])
winner = winner_list[0]

# Print all data
print("Election results :")
print("---------------------")
print("Total Votes: " + str(allVotes))
print("---------------------")
print(str(candidates[0]) + ": " + str(round((percentage_votes[0]), 3)) + "00% " + " (" + str(totalVotes[0]) + ")")
print(str(candidates[1]) + ": " + str(round((percentage_votes[1]), 3)) + "00% " + " (" + str(totalVotes[1]) + ")")
print(str(candidates[2]) + ": " + str(round((percentage_votes[2]), 3)) + "00% " + " (" + str(totalVotes[2]) + ")")
print(str(candidates[3]) + ": " + str(round((percentage_votes[3]), 3)) + "00% " + " (" + str(totalVotes[3]) + ")")
# print(candidates)
# print(percentage_votes)
# print(totalVotes)
print("---------------------")
print("Winner: " + str(winner))
print("---------------------")

# Writing output files

PyPoll = open("output.txt", "w+")
PyPoll.write("Election Results: ")
PyPoll.write('\n' + "Total Votes: " + str(allVotes))
PyPoll.write('\n' + str(
    str(candidates[0]) + ": " + str(round((percentage_votes[0]), 3)) + "00% " + " (" + str(totalVotes[0]) + ")"))
PyPoll.write('\n' + str(
    str(candidates[1]) + ": " + str(round((percentage_votes[1]), 3)) + "00% " + " (" + str(totalVotes[1]) + ")"))
PyPoll.write('\n' + str(
    str(candidates[2]) + ": " + str(round((percentage_votes[2]), 3)) + "00% " + " (" + str(totalVotes[2]) + ")"))
PyPoll.write('\n' + str(
    str(candidates[3]) + ": " + str(round((percentage_votes[3]), 3)) + "00% " + " (" + str(totalVotes[3]) + ")"))
# PyPoll.write('\n' + str(percentage_votes))
# PyPoll.write('\n' + str(totalVotes))
PyPoll.write('\n' + "Winner: " + winner)
