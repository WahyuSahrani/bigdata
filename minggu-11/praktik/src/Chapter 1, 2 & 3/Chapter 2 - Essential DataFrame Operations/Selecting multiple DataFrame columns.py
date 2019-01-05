#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
pd.options.display.max_columns = 40


# In[2]:


movie = pd.read_csv('data/movie.csv')
movie_actor_director = movie[['actor_1_name', 'actor_2_name', 'actor_3_name', 'director_name']]
movie_actor_director.head()


# In[3]:


movie[['director_name']].head()


# In[4]:


movie['actor_1_name', 'actor_2_name', 'actor_3_name', 'director_name']


# In[ ]:




