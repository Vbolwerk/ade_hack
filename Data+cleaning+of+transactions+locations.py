
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
from datetime import datetime


# In[2]:

df = pd.read_csv('DGTL_2016_raw_data_all.csv', sep = ';')


# In[3]:

df.head()


# In[4]:

df = df.loc[:, ['Date Time', 'Store Name', 'Wristband ID']]


# In[5]:

df['Store Name'].value_counts()


# In[6]:

df_wristband_pivot = pd.pivot_table(df, values = 'Date Time', aggfunc='count', index = 'Wristband ID')


# In[7]:

df_wristband_pivot.describe()


# In[8]:

# Converting to Date Time
df['Date Time'] = pd.to_datetime(df['Date Time'])


# In[9]:

# Removing values outside of festival dates
df = df.loc[(df['Date Time']>datetime(2016, 3, 25)) & (df['Date Time']<datetime(2016, 3, 29)), :]


# In[10]:

# Removing SWAPPED & ENTERED for Wristband ID
df = df.loc[(df['Wristband ID']!= 'SWAPPED') & (df['Wristband ID']!= 'ENTERED'), :]


# In[11]:

# Drop duplicate transactions
df = df.drop_duplicates()


# In[12]:

# Sorting observations by Wristband ID & time
df = df.sort_values(['Wristband ID', 'Date Time'])


# In[13]:

df['Store Name'].value_counts()


# In[15]:

# Dictionary which bar belongs to which stage
bar_stage_dict = {'Bar 1A': 'digital',
'Bar 1B': 'digital', 
'Bar 2 - Night': 'analog',
'Bar 2 - Day': 'analog', 
'Bar 3': 'phono',
'Bar 4': 'audio',
'Bar 5': 'stereo',
'Bar 6': 'maeve',
'Bar 7': 'maeve'}


# In[16]:

df['Stage_name'] = df['Store Name'].map(bar_stage_dict)


# In[19]:

df = df.dropna()


# In[ ]:



