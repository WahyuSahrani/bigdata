#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[31]:


movie = pd.read_csv('data/movie.csv')
actor_1_fb_likes = movie['actor_1_facebook_likes']
director = movie['director_name']


# In[32]:


director.value_counts().head(3)


# In[33]:


actor_1_fb_likes.isnull().sum()


# In[34]:


actor_1_fb_likes.dtype


# In[35]:


actor_1_fb_likes.fillna(0)                .astype(int)                .head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




