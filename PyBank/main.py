# -*- coding: UTF-8 -*-
""" Module 3 Challenge - PyBank
    Ilan Goldstein
    2024/12/16
"""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
net_change = []
total_change = []
greatest_inc = [0,0]
greatest_dec = [0,0]

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:
        change = int(row[1])

        # Track the total months
        total_months = total_months+1

        # Track the net change each month
        total_net = total_net + change
        net_change.append(change)

        # Track the monthly change in profit/loss
        if total_months > 1:
            monthly_change = net_change[total_months-1]-net_change[total_months-2]
            total_change.append(monthly_change)

            # Calculate the greatest increase in profits (month and amount)
            if monthly_change > greatest_inc[1]:
                greatest_inc = [row[0], monthly_change]

            # Calculate the greatest decrease in losses (month and amount)
            if monthly_change < greatest_dec[1]:
                greatest_dec = [row[0], monthly_change]

# Calculate the average net change across the months
avg_change = round(sum(total_change)/len(total_change),2)

# Generate the output summary
output = (f'Financial Analysis\n----------------------------\n'
f'Total Months: {total_months}\nTotal: ${total_net}\nAverage Change: ${avg_change}\n'
f'Greatest Increase in Profits: {greatest_inc[0]} (${greatest_inc[1]})\n'
f'Greatest Decrease in Profits: {greatest_dec[0]} (${greatest_dec[1]})')

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
