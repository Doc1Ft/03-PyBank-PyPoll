import os
import csv

bank_csv = os.path.join("Resources", "budget_data.csv")

total_mos = 0
total_net = 0
max_net_change = 0
min_net_change = 0
sumpl = 0
previous_pl = 0
cur_perc_change = 0
diff = 0
diflist = []


# Open and read csv
with open(bank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    #grab first row
    firstrow = next(csvreader)
    #grab prev value from first row
    previous_pl = int(firstrow[1])

    for row in csvreader:  
        total_mos = total_mos + 1
        sumpl = sumpl + int(row[1])
        cur_perc_change = int(row[1])
        diff = cur_perc_change - previous_pl
        diflist.append(diff)
        previous_pl = cur_perc_change
        if cur_perc_change > max_net_change:
            max_net_change = cur_perc_change
            max_month = row[0]
        if cur_perc_change < min_net_change:
            min_net_change = cur_perc_change
            min_month = row[0]

listaverage = (sum(diflist) / total_mos)
print("Financial Review")
print(f"Total Months: {total_mos}")
print(f"Total: {sumpl}")
print(f"Average Change: {listaverage}")
print(f"Greatest Increase in Profits: {max_net_change}")
print(f"Greatest Decrease in Profits: {min_net_change}")

new_file = open("bankresults.txt","w")

new_file.write("Financial Analysis \n")
new_file.write("-------------------------------------------- \n")
new_file.write(f"Total Months: {total_mos} \n")
new_file.write(f"Total: {sumpl} \n")
new_file.write(f"Average Change: {listaverage} \n")
new_file.write(f"Greatest Increase in Profits: {max_net_change} \n")
new_file.write(f"Greatest Decrease in Profits: {min_net_change} \n")

