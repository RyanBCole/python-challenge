#!/usr/bin/env python
# coding: utf-8

# In[50]:


#Modules
import os
import csv


# In[ ]:





# In[51]:


#Variables
months = 0
month_of_change = []
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]
profit_change = 0
profit_average = 0
profit_change_list = []
previous_profit = 0
total_profit = 0
profit = []


# In[52]:


#open the csv file
with open(r'C:\Users\redye\Desktop\python-challenge\PyBank\Resources\budget_data.csv') as csvfile:  
    csvreader = csv.DictReader(csvfile)

    #Start the loop
    for row in csvreader:

        #Count the months
        months += 1

        #Calculate all of the profit
        total_profit = total_profit + int(row["Profit/Losses"])

        #Calculate the average change in profit
        profit_change = float(row["Profit/Losses"])- previous_profit
        previous_profit = float(row["Profit/Losses"])
        profit_change_list = profit_change_list + [profit_change]
        month_of_change = [month_of_change] + [row["Date"]]
       

        #Calculate the greatest increase in profit
        if profit_change>greatest_increase[1]:
            greatest_increase[1]= profit_change
            greatest_increase[0] = row['Date']

        #Calculate the greatest decrease in profit
        if profit_change<greatest_decrease[1]:
            greatest_decrease[1]= profit_change
            greatest_decrease[0] = row['Date']
    profit_average = sum(profit_change_list)/len(profit_change_list)


# In[53]:


with open(r'C:\Users\redye\Desktop\python-challenge\PyBank\main.py.txt', 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % months)
    file.write("Total: $%d\n" % total_profit)
    file.write("Average Change $%d\n" % profit_average)
    file.write("Greatest Increase in Profits: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
    file.write("Greatest Decrease in Profits: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))


# In[54]:


print("Financial Analysis\n")
print("---------------------\n")
print("Total Months: %d\n" % months)
print("Total: $%d\n" % total_profit)
print("Revenue Change $%d\n" % profit_average)
print("Greatest Increase in Profits: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
print("Greatest Decrease in Profits: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))


# In[ ]:





# In[ ]:




