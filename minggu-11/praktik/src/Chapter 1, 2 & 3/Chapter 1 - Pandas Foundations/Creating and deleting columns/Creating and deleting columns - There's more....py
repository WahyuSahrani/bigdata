#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[26]:


profit_index = movie.columns.get_loc('gross') + 1
profit_index


# In[27]:


movie.insert(loc=profit_index,
                 column='profit',
                 value=movie['gross'] - movie['budget'])


# In[28]:


movie.head()


# In[13]:





# In[ ]:





# In[15]:





# In[16]:





# In[ ]:





# In[18]:





# In[19]:





# In[20]:





# In[ ]:





# In[ ]:





# In[ ]:




