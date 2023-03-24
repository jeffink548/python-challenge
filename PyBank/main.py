import csv
import os
#store file
budget_csv = os.path.join("Resources", "budget_data.csv")
print(budget_csv)

# open and read csv data
with open(budget_csv, "r") as csvfile:
 csvreader = csv.reader(csvfile)
 csv_header = next(csvreader)
 dates = []
 profits = []
 for row in csvreader:
   dates.append(row[0])
   profits.append(int(row[1]))
# total months
total_months = len(dates)
#total of profit/losses
total_profit = sum(profits)
#change in profits
changes = []
for i in range(1, len(profits)):
  change = profits[i]- profits[i-1]
  changes.append(change)
#Profits average change
avg_profit_change = sum(changes) / len(changes)
#greeatest increase & decrease in profit
great_increase = max(changes)
great_decrease = min(changes)
great_increase_date = str(dates[changes.index(great_increase)+1])
great_decrease_date = str(dates[changes.index(great_decrease)+1])
#print results 
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${avg_profit_change:.2f}")
print(f"Greatest Increase in Profits: {great_increase_date} (${great_increase})")
print(f"Greatest Decrease in Profits: {great_decrease_date} (${great_decrease})")
#put into text file 
with open('financial_analysis.txt', 'w') as f:
    f.write("Financial Analysis\n")
    f.write("------------------\n")
    f.write(f"Total Months: {total_months}\n")
    f.write(f"Total: ${total_profit}\n")
    f.write(f"Average Change: ${avg_profit_change:.2f}\n")
    f.write(f"Greatest Increase in Profits: {great_increase_date} (${great_increase})\n")
    f.write(f"Greatest Decrease in Profits: {great_decrease_date} (${great_decrease})\n")
    
print("The analysis has been exported to financial_analysis.txt.")
