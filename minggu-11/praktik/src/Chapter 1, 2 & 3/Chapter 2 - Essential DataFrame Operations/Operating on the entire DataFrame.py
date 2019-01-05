#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
pd.options.display.max_columns = 40


# In[18]:


pd.options.display.max_rows = 8
movie = pd.read_csv('data/movie.csv')
movie.shape


# In[19]:


movie.size


# In[20]:


movie.ndim


# In[21]:


len(movie)


# In[22]:


movie.count()


# In[23]:


movie.min()


# In[17]:


movie2 = movie[new_col_order]
movie2.head()


# In[24]:


movie.describe()


# In[25]:


pd.options.display.max_rows = 8


# In[26]:


movie.isnull().sum()


# In[27]:


movie.min(skipna=False)


# In[ ]:




