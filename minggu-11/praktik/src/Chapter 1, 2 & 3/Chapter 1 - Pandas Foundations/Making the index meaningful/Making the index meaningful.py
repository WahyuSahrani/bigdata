#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[39]:


movie = pd.read_csv('data/movie.csv')


# In[38]:


movie.shape


# In[40]:


movie2 = movie.set_index('movie_title')
movie2


# In[41]:


pd.read_csv('data/movie.csv', index_col='movie_title')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




