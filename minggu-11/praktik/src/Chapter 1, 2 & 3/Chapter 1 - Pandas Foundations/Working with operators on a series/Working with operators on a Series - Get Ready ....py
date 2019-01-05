#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[13]:


movie = pd.read_csv('data/movie.csv')
imdb_score = movie['imdb_score']
imdb_score


# In[14]:


imdb_score + 1


# In[15]:


imdb_score * 2.5


# In[16]:


imdb_score // 7


# In[17]:


imdb_score > 7


# In[18]:


director = movie['director_name']


# In[19]:


director == 'James Cameron'


# In[ ]:





# In[ ]:





# In[ ]:




