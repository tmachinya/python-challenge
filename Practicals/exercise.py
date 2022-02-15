import csv

with open('election_data.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    next(data, None)
    totalVotes = 0
    for row in data:
        # print(row[1])
        totalVotes += 1
    print("total votes: " + str(totalVotes))

