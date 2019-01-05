#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
pd.options.display.max_columns = 40


# In[6]:


movie = pd.read_csv('data/movie.csv', index_col='movie_title')
movie.get_dtype_counts()


# In[7]:


movie.select_dtypes(include=['int']).head()


# In[8]:


movie.select_dtypes(include=['number']).head()


# In[9]:


movie.filter(like='facebook').head()


# In[10]:


movie.filter(regex='\d').head()


# In[11]:


movie.filter(items=['actor_1_name', 'asdf']).head()


# In[ ]:




