#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
pd.options.display.max_columns = 40


# In[3]:


movie = pd.read_csv('data/movie.csv')
movie.isnull().head()


# In[4]:


movie.isnull().sum().head()


# In[5]:


movie.isnull().any().any()


# In[6]:


movie.isnull().get_dtype_counts()


# In[ ]:




