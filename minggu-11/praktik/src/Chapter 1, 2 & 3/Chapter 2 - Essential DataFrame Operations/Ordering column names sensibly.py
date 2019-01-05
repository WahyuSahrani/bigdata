#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
pd.options.display.max_columns = 40


# In[12]:


movie = pd.read_csv('data/movie.csv')


# In[13]:


movie.head()


# In[14]:


movie.columns


# In[15]:


disc_core = ['movie_title','title_year', 'content_rating','genres']
disc_people = ['director_name','actor_1_name', 'actor_2_name','actor_3_name']
disc_other = ['color','country','language','plot_keywords','movie_imdb_link']
cont_fb = ['director_facebook_likes','actor_1_facebook_likes','actor_2_facebook_likes',
           'actor_3_facebook_likes', 'cast_total_facebook_likes', 'movie_facebook_likes']
cont_finance = ['budget','gross']
cont_num_reviews = ['num_voted_users','num_user_for_reviews', 'num_critic_for_reviews']
cont_other = ['imdb_score','duration', 'aspect_ratio', 'facenumber_in_poster']


# In[16]:


new_col_order = disc_core + disc_people + disc_other +                     cont_fb + cont_finance + cont_num_reviews + cont_other
set(movie.columns) == set(new_col_order)


# In[11]:


movie.filter(items=['actor_1_name', 'asdf']).head()


# In[17]:


movie2 = movie[new_col_order]
movie2.head()


# In[ ]:




