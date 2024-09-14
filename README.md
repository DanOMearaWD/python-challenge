# python-challenge

This project analyzes two different CSV files:<br />

budget_data.csv ([PyBank/Resources]):<br />
This dataset consists of two columns: "Date" and "Profit/Losses". The Python script [PyBank/main.py] processes this file to calculate the following:<br />

Total number of months in the dataset<br />
Net total amount of "Profit/Losses" over the entire period<br />
Changes in "Profit/Losses" over the period and the average of these changes<br />
Greatest increase in profits (date and amount) over the period<br />
Greatest decrease in profits (date and amount) over the period<br />
The results are printed to the console and saved in [PyBank/analysis].<br />

election_data.csv ([PyPoll/Resources]):<br />
This dataset includes three columns: "Voter ID", "County", and "Candidate". The Python script [PyPoll/main.py] analyzes this data to determine:<br />

Total number of votes cast<br />
Complete list of candidates who received votes<br />
Percentage of votes each candidate won<br />
Total number of votes each candidate won<br />
Winner of the election based on popular vote<br />
The results are printed to the console and saved in [PyPoll/analysis].<br />
