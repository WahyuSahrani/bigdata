#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[ ]:


movie = pd.read_csv('data/movie.csv')


# In[28]:


director = movie['director_name'] # save Series to variable
director.name


# In[29]:


director.to_frame().head()


# In[ ]:




