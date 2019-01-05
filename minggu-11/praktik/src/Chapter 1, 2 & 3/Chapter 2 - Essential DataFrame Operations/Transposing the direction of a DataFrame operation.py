#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
pd.options.display.max_columns = 40


# In[36]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')
college_ugds_ = college.filter(like='UGDS_')
college_ugds_.head()


# In[37]:


college_ugds_.count()


# In[38]:


college_ugds_.count(axis=0)


# In[39]:


college_ugds_.count(axis='index')


# In[40]:


college_ugds_.count(axis='columns').head()


# In[41]:


college_ugds_.median(axis='index')


# In[42]:


college_ugds_cumsum = college_ugds_.cumsum(axis=1)
college_ugds_cumsum.head()


# In[43]:


college_ugds_cumsum.sort_values('UGDS_HISP', ascending=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[34]:





# In[ ]:





# In[ ]:




