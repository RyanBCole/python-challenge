#!/usr/bin/env python
# coding: utf-8

# In[40]:


import csv
import os


# In[41]:


election_data_csv = os.path.join("C:\\Users\\redye\\Documents\\election_data.csv")


# In[42]:


#Variables
total_votes = 0
candidates = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# In[43]:


#Open the file. 
with open(r'C:\Users\redye\Desktop\python-challenge\PyPoll\Resources\election_data.csv') as election_data:
    
    file_reader = csv.reader(election_data)

    #Print the header row. 
    headers = next(file_reader)
    
    #Start the loop
    for row in file_reader:
        #Add vote count. 
        total_votes += 1

        #Print the candidate name
        candidate_name = row[2]

        #Add candidate if not already listed
        if candidate_name not in candidates: 
            candidates.append(candidate_name) 
            candidate_votes[candidate_name] = 0
        
        #Add a vote to that candidate 
        candidate_votes[candidate_name] += 1
    
    #Print the count 
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n")
    print(election_results, end="") 
  
    #Calculate and print the percentage of votes a candidate receives
    for candidate_name in candidate_votes:  
        votes = candidate_votes[candidate_name] 
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n") 
        print(candidate_results)

        #Calculate winning vote count
        if (votes > winning_count) and (vote_percentage > winning_percentage): 
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    #Determine Winner
    winner = (
        f"-----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------\n")
    print(winner)


# In[39]:


#Export to file
with open(r'C:\Users\redye\Desktop\python-challenge\PyPoll\main.py.txt', 'w') as file:
    file.write(election_results)
    file.write(candidate_results)
    file.write(winner)


# In[ ]:




