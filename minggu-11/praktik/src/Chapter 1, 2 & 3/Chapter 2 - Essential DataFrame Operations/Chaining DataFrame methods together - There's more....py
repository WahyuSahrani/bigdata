#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
pd.options.display.max_columns = 40


# In[7]:


movie = pd.read_csv('data/movie.csv')
movie[['color', 'movie_title', 'color']].max()


# In[8]:


movie.select_dtypes(['object']).fillna('').max()


# In[ ]:





# In[ ]:





# In[ ]:




