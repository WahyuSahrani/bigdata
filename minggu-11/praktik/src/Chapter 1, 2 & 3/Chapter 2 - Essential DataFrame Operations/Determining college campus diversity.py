#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
pd.options.display.max_columns = 40


# In[44]:


pd.read_csv('data/college_diversity.csv', index_col='School')


# In[45]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')
college_ugds_ = college.filter(like='UGDS_')
college_ugds_.head()


# In[46]:


college_ugds_.isnull().sum(axis=1).sort_values(ascending=False).head()


# In[47]:


college_ugds_ = college_ugds_.dropna(how='all')


# In[48]:


college_ugds_.isnull().sum()


# In[49]:


college_ugds_.ge(.15).head()


# In[50]:


diversity_metric = college_ugds_.ge(.15).sum(axis='columns')
diversity_metric.head()


# In[51]:


diversity_metric.value_counts()


# In[52]:


diversity_metric.sort_values(ascending=False).head()


# In[53]:


college_ugds_.loc[['Regency Beauty Institute-Austin', 
                          'Central Texas Beauty College-Temple']]


# In[54]:


us_news_top = ['Rutgers University-Newark', 
               'Andrews University', 
               'Stanford University', 
               'University of Houston',
               'University of Nevada-Las Vegas']


# In[55]:


diversity_metric.loc[us_news_top]


# In[56]:


college_ugds_.max(axis=1).sort_values(ascending=False).head(10)


# In[57]:


college_ugds_.loc['Talmudical Seminary Oholei Torah']


# In[58]:


(college_ugds_ > .01).all(axis=1).any()


# In[ ]:




