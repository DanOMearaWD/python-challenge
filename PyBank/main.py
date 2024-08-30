import csv #Module for reading csv files
csvpath = "Resources/budget_data.csv" #relative path for csv file

#Read csv file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    #skip header row
    next(csvreader)
    
    #loop through csv rows
    rowcount = 0
    total_profits_losses = 0
    previous_profit = 0
    change_profits_losses = {}
    for row in csvreader:
        rowcount += 1   #Add 1 to row count
        total_profits_losses += int(row[1]) #row[1] is Profit/Losses for each row converted to int

        #add keys and values to dict of change in profits - cant compare previous value in first row
        if rowcount > 1:
            change_profits_losses[row[0]] = int(row[1]) - previous_profit
        previous_profit = int(row[1])
    
    #average = sum of change in profits values as list / length of changes in profits as list & rounded to 2 decimal places
    average_change_profits_losses = round(sum(list(change_profits_losses.values()))/len(list(change_profits_losses.values())),2)
    
    #need max and min values so zip values, keys of change_profits_losses to use for max() and min() calcs !put zip inside list so it doesnt dissappear
    change_profits_losses_zip = list(zip(change_profits_losses.values(), change_profits_losses.keys()))


    #Get max and min change in profits/losses
    max_change_profits_losses = max(change_profits_losses_zip)
    min_change_profits_losses = min(change_profits_losses_zip)

    
    
    #print to terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {rowcount}")
    print(f"Total: ${total_profits_losses}")
    print(f"Average Change: ${average_change_profits_losses}")
    # max_ and min_ change_profits_losses format = (1862002, 'Aug-16')
    print(f"Greatest Increase in Profits: {max_change_profits_losses[1]} (${max_change_profits_losses[0]})")
    print(f"Greatest Decrease in Profits: {min_change_profits_losses[1]} (${min_change_profits_losses[0]})")

    #export text file
    outputpath = "analysis/financial_analysis.txt" #relative path for txt file
    with open(outputpath, 'w') as textfile:
        textfile.write("Financial Analysis" + "\n") # + "\n" adds newline
        textfile.write("----------------------------" + "\n")
        textfile.write(f"Total Months: {rowcount}" + "\n")
        textfile.write(f"Total: ${total_profits_losses}" + "\n")
        textfile.write(f"Average Change: ${average_change_profits_losses}" + "\n")
        # max_ and min_ change_profits_losses format = (1862002, 'Aug-16')
        textfile.write(f"Greatest Increase in Profits: {max_change_profits_losses[1]} (${max_change_profits_losses[0]})" + "\n")
        textfile.write(f"Greatest Decrease in Profits: {min_change_profits_losses[1]} (${min_change_profits_losses[0]})" + "\n")