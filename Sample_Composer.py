#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import random
import Constants


# In[2]:


# Constants
OUTPUT_FILE_PATH = '.\\data\\sample\\sample_1.xlsx'
TOTAL_ROWS = 1000

NAMES_FILE_PATH = '.\\data\\resources\\names.csv'

NAMES = pd.read_csv(NAMES_FILE_PATH, header=None).T.values[0]


# In[4]:


# Get randomized rows
rows_list = list()
for i in range(TOTAL_ROWS):
    row = dict()
    row['First Name'] = random.choice(NAMES)
    row['Last Name'] = random.choice(NAMES)
    row['Dept'] = random.choice(Constants.DEPTS)
    row['Major Code'] = random.choice(Constants.DEPTS_MAJORS[row['Dept']])
    row['Class Standing'] = random.choice(Constants.CLASS_STANDINGS)
    row['Cum GPA'] = round(random.random() * 4, 5)
    row['Email'] = row['First Name'].lower() + row['Last Name'][0].lower() + '@ucsd.edu'
    rows_list.append(row)

# Create DF
df = pd.DataFrame(rows_list, columns=Constants.COLUMNS)

# View DF
df.head()


# In[5]:


# Output DF
df.to_excel(OUTPUT_FILE_PATH, index=False)


# In[ ]:




