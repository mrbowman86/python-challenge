# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis","budget_analysis.txt")

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
prior_net = 0
profit_changes = []
max_increase = ["",0]
max_decrease = ["",999999999]

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    prior_net = int(first_row[1])

    # Track the total and net change

    # Process each row of data
    for row in reader:
        date = row[0]
        net = int(row[1])

        # Track the total
        total_months += 1
        total_net += net

        # Track the net change
        net_change = net - prior_net
        prior_net = net
        profit_changes.append(net_change)

        # Calculate the greatest increase in profits (month and amount)
        if net_change > max_increase[1]:
            max_increase[0] = date
            max_increase[1] = net_change

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < max_decrease[1]:
            max_decrease[0] = date
            max_decrease[1] = net_change

# Calculate the average net change across the months
average_change = sum(profit_changes) / len(profit_changes)

# Generate the output summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change: 2f}\n"
    f"Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})\n"
    f"Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)