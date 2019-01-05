#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[38]:


movie = pd.read_csv('data/movie.csv')


# In[63]:


actor_1_fb_likes.quantile(.2)


# In[64]:


actor_1_fb_likes.quantile([.1, .2, .3, .4, .5, .6, .7, .8, .9])


# In[65]:


director.isnull()


# In[66]:


actor_1_fb_likes_filled = actor_1_fb_likes.fillna(0)
actor_1_fb_likes_filled.count()


# In[68]:


actor_1_fb_likes_dropped = actor_1_fb_likes.dropna()
actor_1_fb_likes_dropped.size


# In[ ]:





# In[ ]:




