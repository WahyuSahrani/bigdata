#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[6]:


movie = pd.read_csv('data/movie.csv')


# In[12]:


movie['has_seen'] = 0


# In[11]:


movie.columns


# In[13]:


movie['actor_director_facebook_likes'] = (movie['actor_1_facebook_likes'] + 
                                              movie['actor_2_facebook_likes'] + 
                                              movie['actor_3_facebook_likes'] + 
                                              movie['director_facebook_likes'])


# In[14]:


movie['actor_director_facebook_likes'].isnull().sum()


# In[15]:


movie['actor_director_facebook_likes'] = movie['actor_director_facebook_likes'].fillna(0)


# In[16]:


movie['is_cast_likes_more'] = (movie['cast_total_facebook_likes'] >= 
                                  movie['actor_director_facebook_likes'])


# In[17]:


movie['is_cast_likes_more'].all()


# In[18]:


movie = movie.drop('actor_director_facebook_likes', axis='columns')


# In[19]:


movie['actor_total_facebook_likes'] = (movie['actor_1_facebook_likes'] + 
                                       movie['actor_2_facebook_likes'] + 
                                       movie['actor_3_facebook_likes'])

movie['actor_total_facebook_likes'] = movie['actor_total_facebook_likes'].fillna(0)


# In[20]:


movie['pct_actor_cast_like'] = (movie['actor_total_facebook_likes'] / 
                                movie['cast_total_facebook_likes'])


# In[24]:


movie['pct_actor_cast_like'].min(), movie['pct_actor_cast_like'].max() 


# In[ ]:





# In[ ]:




