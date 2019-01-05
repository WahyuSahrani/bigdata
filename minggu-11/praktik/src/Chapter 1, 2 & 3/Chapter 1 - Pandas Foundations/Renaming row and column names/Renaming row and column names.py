#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


movie = pd.read_csv('data/movie.csv', index_col='movie_title')


# In[4]:


idx_rename = {'Avatar':'Ratava', 'Spectre': 'Ertceps'} 
col_rename = {'director_name':'Director Name', 
              'num_critic_for_reviews': 'Critical Reviews'}


# In[5]:


movie.rename(index=idx_rename, 
             columns=col_rename).head()


# In[ ]:




