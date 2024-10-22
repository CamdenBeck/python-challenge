# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0

# Add more variables to track other necessary financial data
total = 0
months_list = []
monthly_profits = []
monthly_net = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Process each row of data
    current_row_num = 1
    for row in reader:
        total_months += 1

        # Track the total
        total += int(row[1])
        # monthly_totals.append(total)

        # Track the net change
        if current_row_num > 1:
            net_profit = int(row[1]) - monthly_profits[-1]
            monthly_net.append(net_profit)
            months_list.append(row[0])

        monthly_profits.append(int(row[1]))
        current_row_num += 1

    # Calculate the greatest increase in profits (month and amount)
    max_profit = max(monthly_net)
    max_month_index = monthly_net.index(max_profit)
    max_increase_month = months_list[max_month_index]

    # Calculate the greatest decrease in losses (month and amount)
    max_loss = min(monthly_net)
    min_month_index = monthly_net.index(max_loss)
    max_decrease_month = months_list[min_month_index]

# Calculate the average net change across the months
average_net = sum(monthly_net)/len(monthly_net)

# Generate the output summary
output = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total}
Average Change: ${average_net}
Greatest Increase in Profits: {max_increase_month} (${max_profit})
Greatest Decrease in Profits: {max_decrease_month} (${max_loss})"""

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
