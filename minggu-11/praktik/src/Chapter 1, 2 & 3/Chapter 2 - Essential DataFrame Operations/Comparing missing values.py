#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
pd.options.display.max_columns = 40


# In[21]:


np.nan == np.nan


# In[22]:


None == None


# In[23]:


5 > np.nan


# In[24]:


np.nan > 5


# In[25]:


5 != np.nan


# In[27]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')
college_ugds_ = college.filter(like='UGDS_')


# In[28]:


college_ugds_.head() == .0019


# In[29]:


college_self_compare = college_ugds_ == college_ugds_
college_self_compare.head()


# In[30]:


college_self_compare.all()


# In[19]:


college_ugds_op_round.equals(college_ugds_round)


# In[31]:


(college_ugds_ == np.nan).sum()


# In[32]:


college_ugds_.isnull().sum()


# In[33]:


from pandas.testing import assert_frame_equal


# In[34]:


assert_frame_equal(college_ugds_, college_ugds_)


# In[35]:


college_ugds_.eq(.0019).head()


# In[ ]:




