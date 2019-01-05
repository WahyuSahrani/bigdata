#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[20]:


imdb_score.add(1)              # imdb_score + 1


# In[21]:


imdb_score.mul(2.5)            # imdb_score * 2.5


# In[22]:


imdb_score.floordiv(7)         # imdb_score // 7


# In[23]:


imdb_score.gt(7)               # imdb_score > 7


# In[24]:


director.eq('James Cameron')   # director == 'James Cameron'


# In[18]:


director = movie['director_name']


# In[19]:


director.eq('James Cameron')   # director == 'James Cameron'


# In[25]:


imdb_score.astype(int).mod(5)


# In[26]:


a = type(1)


# In[27]:


type(a)


# In[28]:


a = type(imdb_score)


# In[29]:


a([1,2,3])


# In[ ]:




