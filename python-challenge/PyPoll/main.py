import csv
import os

#creating lists
total_votes = []
total_candidates = []
maxvote_winner = []
vote_percent=[]
#using dictionary to get each candidate name 
poll={}

#filepath
csvpath=os.path.join('election_data.csv')
   


#open file 

with open(csvpath,'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    next(csvreader, None)
#appending votes  and total candidates  
    
    for row in csvreader:
      total_votes.append(row[0])
      if row[2] in poll.keys():
          poll[row[2]]=poll[row[2]]+1
      else:
          poll[row[2]]=1
    #create dictionary keys and values and add them to list
    for key,value in poll.items():
       total_candidates.append(key)
       maxvote_winner.append(value)
    #find percentage of votes
    for n in maxvote_winner:
      vote_percent.append(round(n/len(total_votes)*100,1))
      
   
    print (f'{vote_percent[0]},{total_candidates[0]}') 
    print(f'Total votes :{len(total_votes)}')
    
    
        