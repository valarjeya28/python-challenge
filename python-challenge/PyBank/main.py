import csv
import os

#creating lists
total_months = []
total_profit = []
monthly_profit_change = []
#filepath
csvpath=os.path.join('budget_data.csv')
def pybank(pydata):
    for i in range (len(total_profit)-1):
     monthly_profit_change.append(total_profit[i+1]-total_profit[i])
#find average for monthly Profit change
    average=round(float(sum(monthly_profit_change)/len(monthly_profit_change)),2)
    greatestincrease=max(monthly_profit_change)
    greatest_index=total_profit.index(max(total_profit))
    #finding   month for  max profits by index of total profit
    greatest_month=total_months[greatest_index]
    #finding month for min profit by index of total profit
    greatestdecrease=min(monthly_profit_change)
    greatest_decrease_index=total_profit.index(min(total_profit))
    greatest_decrease_month=total_months[greatest_decrease_index]
    results=(
    f"Financial Analysis \n"
    f"-------------------------------------- \n"
    f"Total months :{len(total_months)} \n"
    f"Total: ${sum(total_profit)} \n"
    f"Average  Change: {average} \n"
    f"Greatest Increase in Profits: {greatest_month} (${int(greatestincrease)}) \n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${int(greatestdecrease)}) \n")
    print(results)
    outputfile= os.path.join("output.txt")
    with open(outputfile,'w') as txtfile:
        txtwriter=txtfile.write(results)
#open file 
with open(csvpath,'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    next(csvreader, None)
    #appending months  and total profits 
    for row in csvreader:
     total_months.append(row[0])
     total_profit.append(int(row[1]))
    pybank(csvreader)
    




 






