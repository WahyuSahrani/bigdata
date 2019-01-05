#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[6]:


movie = pd.read_csv('data/movie.csv', index_col='movie_title')
index = movie.index
columns = movie.columns

index_list = index.tolist()
column_list = columns.tolist()

index_list[0] = 'Ratava'
index_list[2] = 'Ertceps'
column_list[1] = 'Director Name'
column_list[2] = 'Critical Reviews'


# In[7]:


print(index_list[:5])


# In[5]:


movie.rename(index=idx_rename, 
             columns=col_rename).head()


# In[8]:


print(column_list)


# In[9]:


movie.index = index_list
movie.columns = column_list


# In[10]:


movie.head()


# In[ ]:




