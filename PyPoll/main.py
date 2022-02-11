import os
import csv

# path to the csvfile
csvpath = os.path.join('election_data.csv')

# initializing the variables
pollData = {}
allVotes = 0
with open(csvpath, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    next(csvread, None)

    for row in csvread:
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
    percentage_votes.append(round(n / allVotes * 100, 1))

# Finding the winner
clean_data = list(zip(candidates, totalVotes, percentage_votes))

winner_list = []
for name in clean_data:
    if max(totalVotes) == name[1]:
        winner_list.append(name[0])
winner = winner_list[0]

# Print all data
print("Election results :")
print(allVotes)
print(candidates)
print(percentage_votes)
print(totalVotes)
print(winner)

# Writng output files
PyPoll = open("output.txt", "w+")
PyPoll.write("Election Results")
PyPoll.write('\n' + "allVotes" + str(allVotes))
PyPoll.write('\n' + str(candidates))
PyPoll.write('\n' + str(percentage_votes))
PyPoll.write('\n' + str(totalVotes))
PyPoll.write('\n' + "Winner:" + winner)







