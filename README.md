# python-challenge

This project analyzes two different CSV files:

budget_data.csv ([PyBank/Resources]):
This dataset consists of two columns: "Date" and "Profit/Losses". The Python script [PyBank/main.py] processes this file to calculate the following:

Total number of months in the dataset
Net total amount of "Profit/Losses" over the entire period
Changes in "Profit/Losses" over the period and the average of these changes
Greatest increase in profits (date and amount) over the period
Greatest decrease in profits (date and amount) over the period
The results are printed to the console and saved in [PyBank/analysis].

election_data.csv ([PyPoll/Resources]):
This dataset includes three columns: "Voter ID", "County", and "Candidate". The Python script [PyPoll/main.py] analyzes this data to determine:

Total number of votes cast
Complete list of candidates who received votes
Percentage of votes each candidate won
Total number of votes each candidate won
Winner of the election based on popular vote
The results are printed to the console and saved in [PyPoll/analysis].
