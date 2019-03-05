import csv
import os

#creating lists
total_votes = []
total_candidates = []
maxvote_winner = []
#filepath
csvpath=os.path.join('election_data.csv')
def pollvotes()



#open file 
with open(csvpath,'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    next(csvreader, None)