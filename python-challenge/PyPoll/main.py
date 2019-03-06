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
      percent = float(n/len(total_votes)*100)
      vote_percent.append(round(percent,2))
    
     #zips candidates,vote_percent and vote_count into tuples
    poll_data=list(zip(total_candidates,vote_percent,vote_count))
     
      
    #find highest vote count winner
    
    winner_List=[]
    for vote in poll_data:
       if max(vote_count) == vote[2]:
            winner_List.append(vote[0])
    winner=winner_List[0]    

    #----------Election Results--------------------------
 

    outputfile= os.path.join("output.txt")
    with open(outputfile,'w') as txtfile:
        txtfile.writelines('Election Results \n-------------------------\nTotal votes : '+str(len(total_votes))+
            '\n--------------------------------\n')
        for entry in poll_data:
            txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
        txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

    with open(outputfile, 'r') as readfile:
        print(readfile.read())
    
   
    
    
        