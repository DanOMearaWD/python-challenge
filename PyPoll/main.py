import csv #Module for reading csv files
csvpath = "Resources/election_data.csv" #relative path for csv file

#Read csv file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    #skip header row
    next(csvreader)

    #loop through csv rows
    rowcount = 0
    candidates = {} 
    for row in csvreader:
        rowcount += 1   #Add 1 to row count

        #Candidate in dict add votes
        if row[2] in candidates:
            candidates[row[2]] += 1
        else: #Candidate not in dict - add name and number votes
            candidates[row[2]] = 1

            
    most_votes = 0
    winner = ""


    print("Election Results") 
    print("-------------------------")
    print(f"Total Votes: {rowcount}")
    print("-------------------------")
    #get each item from candidates dict and loop through key and value pairs
    for x,y in candidates.items():
        #print name: percent of votes rounded to 3 decimal places (number of votes)
        print(f"{x}: {round((y/rowcount)*100,3)}% ({y})")
        #Get most votes and save winner with most votes
        if y > most_votes:
            most_votes = y
            winner = x
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")


    #export text file
    outputpath = "analysis/election_analysis.txt" #relative path for txt file
    with open(outputpath, 'w') as textfile:
        textfile.write("Election Results" + "\n") # + "\n" adds newline
        textfile.write("-------------------------" + "\n")
        textfile.write(f"Total Votes: {rowcount}" + "\n")
        textfile.write("-------------------------" + "\n")
        #get each item from candidates dict and loop through key and value pairs
        for x,y in candidates.items():
            #print name: percent of votes rounded to 3 decimal places (number of votes)
            textfile.write(f"{x}: {round((y/rowcount)*100,3)}% ({y})" + "\n")
            #Get most votes and save winner with most votes
            if y > most_votes:
                most_votes = y
                winner = x
        textfile.write("-------------------------" + "\n")
        textfile.write(f"Winner: {winner}" + "\n")
        textfile.write("-------------------------" + "\n")