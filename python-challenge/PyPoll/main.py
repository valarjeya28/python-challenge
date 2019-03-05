import csv
import os

#creating lists
total_votes = []
total_candidates = []
maxvote_winner = []

#filepath
csvpath=os.path.join('election_data.csv')
   


#open file 

with open(csvpath,'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    next(csvreader, None)
#appending votes  and total candidates  
    
    for row in csvreader:
      total_votes.append(row[0])
    print(f'Total votes :{len(total_votes)}')
        