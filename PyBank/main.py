# import file

import os
import csv

# path to the csvfile

csvpath = os.path.join('budget_data.csv')

# initializing the variables
allMonths = 0
totalRevenue = 0
changes = []
dateCount = []
greatest_inc = 0
greatest_inc_month = 0
greatest_dec = 0
greatest_dec_month = 0

# Open the CSV
with open(csvpath, newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    next(data, None)
    row = next(data)
    # calculating the total number of months and total revenue
    previous_profit = int(row[1])
    allMonths = allMonths + 1
    totalRevenue = totalRevenue + int(row[1])
    greatest_inc = int(row[1])
    greatest_inc_month = row[0]

    for row in data:

        allMonths = allMonths + 1
        totalRevenue = totalRevenue + int(row[1])

        # Calculate change from this month to previous months
        change = int(row[1]) - previous_profit
        changes.append(change)
        previous_profit = int(row[1])
        dateCount.append(row[0])

        # calculating the greatest increase
        if int(row[1]) > greatest_inc:
            greatest_inc = int(row[1])
            greatest_inc_month = row[0]

        # calculating the greatest decrease
        if int(row[1]) < greatest_dec:
            greatest_dec = int(row[1])
            greatest_dec_month = row[0]

            # calculating the average and date
    average_change = sum(changes) / len(changes)

    high = max(changes)
    low = min(changes)

    # printing all values
    print("Financial Analysis")
    print("Total Months:" + str(allMonths))
    print("Total Amount:" + str(totalRevenue))
    print(average_change)
    print(greatest_inc_month, max(changes))
    print(greatest_dec_month, min(changes))

# writing output files
PyBank = open("output.txt", "w+")
PyBank.write("Financial Analysis")
PyBank.write('\n' + "Total Months" + str(allMonths))
PyBank.write('\n' + "Total Amount" + str(totalRevenue))
PyBank.write('\n' + "Average" + str(average_change))
PyBank.write('\n' + greatest_inc_month)
PyBank.write('\n' + str(high))
PyBank.write('\n' + greatest_dec_month)
PyBank.write('\n' + str(low))












