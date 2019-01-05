#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
pd.options.display.max_columns = 40


# In[9]:


college = pd.read_csv('data/college.csv')
college + 5


# In[11]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')
college_ugds_ = college.filter(like='UGDS_')


# In[12]:


college == 'asdf'


# In[13]:


college_ugds_.head()


# In[14]:


college_ugds_.head() + .00501


# In[15]:


(college_ugds_.head() + .00501) // .01


# In[16]:


college_ugds_op_round = (college_ugds_ + .00501) // .01 / 100
college_ugds_op_round.head()


# In[17]:


college_ugds_round = (college_ugds_ + .00001).round(2)
college_ugds_round.head()


# In[18]:


.045 + .005


# In[19]:


college_ugds_op_round.equals(college_ugds_round)


# In[ ]:





# In[ ]:




