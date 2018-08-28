
# coding: utf-8

# In[2]:


import csv
f = open("guns.csv", "r")
data = list(csv.reader(f))
print(data[0:5])


# # HI
# ## HMMMMM
# 

# In[3]:



headers = data[0]
data = data[1:]
print(headers)
print(data[0:5])


# In[1]:


year_counts = {}
years = [rows[1] for rows in data]
for item in years:
    if item in year_counts:
        year_counts[item] += 1
    else:
        year_counts[item] = 1
print(year_counts)
    
    


# In[7]:


import datetime

dates = []
for row in data:
    date = datetime.datetime(row[1], row[2], weekday= 1)
    dates.append(date)
print(dates[0:5])


# In[8]:


date_counts = {}
for date in dates:
    if date not in date_counts:
        date_counts[date] = 0
    date_counts[date] += 1
    
date_counts


# In[2]:


def get_counts(data, column):
    ret_list = {}
    gathered_data = [row[column] for row in data]
    for item1 in gathered_data:
        if item1 not in specific_list:
            specific_list[item1] = 0
        specific_list[item1] += 1
    return specific_list
gender_counts = get_counts(data, 5)
race_counts = get_counts(data, 7)
gender_counts
race_counts

