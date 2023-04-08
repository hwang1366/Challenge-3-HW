import os
import csv


budget_data = os.path.join("budget_data.csv")

total_months = 0
total_profits = 0
value = 0
change = 0
dates = []
profits = []


with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    first_row = next(csvreader)
    total_months += 1
    total_profits += int(first_row[1])
    value = int(first_row[1])
 
    for row in csvreader:
       
        dates.append(row[0])
        
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        total_months += 1
        total_profits = total_profits + int(row[1])

    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]
  
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    avg_change = sum(profits)/len(profits)
    
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_profits)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

output = open("output.txt", "w")

output1 = "Financial Analysis"
output2 = "---------------------"
output3 = str(f"Total Months: {str(total_months)}")
output4 = str(f"Total: ${str(total_profits)}")
output5 = str(f"Average Change: ${str(round(avg_change,2))}")
output6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
output7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(output1,output2,output3,output4,output5,output6,output7))