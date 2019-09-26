#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import Constants


# In[2]:


# Constants
INPUT_FILE_PATH = '.\\data\\sample\\sample_1.xlsx'


# In[5]:


# Import data file
df = pd.read_excel(INPUT_FILE_PATH)

df.head()


# In[10]:


result_df = pd.DataFrame()

for dept in Constants.DEPTS:
    single_dept = df[df['Dept'] == dept]
    filtered = pd.DataFrame()
    
    for major in Constants.DEPTS_MAJORS[dept]:
        single_major = df[df['Major Code'] == major]
        filtered = filtered.append(single_major, ignore_index=True)
        
        for standing in Constants.CLASS_STANDINGS:
            single_standing = filtered[filtered['Class Standing'] == standing]
            top_n = single_standing.quantile(Constants.CLASS_QUANTILE[standing])[0]
            top_n = single_standing[single_standing['Cum GPA'] >= top_n]
            result_df = result_df.append(top_n, ignore_index=True)

result_df = result_df[['First Name', 'Last Name', 'Major Code', 'Dept', 'Email']]


# In[11]:


result_df.to_excel('results.xlsx', index=False)


# In[ ]:




