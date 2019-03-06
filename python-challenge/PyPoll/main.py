import csv
import os

#creating lists
total_votes = []
total_candidates = []
vote_count = []
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
       vote_count.append(value)
    #find percentage of votes
    for n in vote_count:
      vote_percent.append(round((n/len(total_votes)*100),3))

     #zips candidates,vote_percent and vote_count into tuples
    poll_data=list(zip(total_candidates,vote_percent,vote_count))
     
     
    
    
      
    #find highest vote count winner
    #for i in vote_count:
     # if i >  i+1 :
      #  print (f'{vote_percent[i]},{total_candidates[i]}') 
    winner_List=[]
    for vote in poll_data:
       if max(vote_count) == vote[2]:
            winner_List.append(vote[0])
    winner=winner_List[0]    
    print(winner)
    print(f'Total votes :{len(total_votes)}')
     #from poll data we are getting winner list
    for i in poll_data:
      print(f'{i[0]} :{i[1]} % ({i[2]})')

    #winner
    
    
    #print (f'{vote_percent[0]},{total_candidates[0]}') 
   
    
    
        