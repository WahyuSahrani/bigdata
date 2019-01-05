

```python
import pandas as pd
import numpy as np
```


```python
movie = pd.read_csv('data/movie.csv')
```


```python
movie['has_seen'] = 0
```


```python
movie.columns
```




    Index(['color', 'Director Name', 'Critical Reviews', 'duration',
           'director_facebook_likes', 'actor_3_facebook_likes', 'actor_2_name',
           'actor_1_facebook_likes', 'gross', 'genres', 'actor_1_name',
           'num_voted_users', 'cast_total_facebook_likes', 'actor_3_name',
           'facenumber_in_poster', 'plot_keywords', 'movie_imdb_link',
           'num_user_for_reviews', 'language', 'country', 'content_rating',
           'budget', 'title_year', 'actor_2_facebook_likes', 'imdb_score',
           'aspect_ratio', 'movie_facebook_likes'],
          dtype='object')




```python
movie['actor_director_facebook_likes'] = (movie['actor_1_facebook_likes'] + 
                                              movie['actor_2_facebook_likes'] + 
                                              movie['actor_3_facebook_likes'] + 
                                              movie['director_facebook_likes'])
```


```python
movie['actor_director_facebook_likes'].isnull().sum()
```




    122




```python
movie['actor_director_facebook_likes'] = movie['actor_director_facebook_likes'].fillna(0)
```


```python
movie['is_cast_likes_more'] = (movie['cast_total_facebook_likes'] >= 
                                  movie['actor_director_facebook_likes'])
```


```python
movie['is_cast_likes_more'].all()
```




    False




```python
movie = movie.drop('actor_director_facebook_likes', axis='columns')
```


```python
movie['actor_total_facebook_likes'] = (movie['actor_1_facebook_likes'] + 
                                       movie['actor_2_facebook_likes'] + 
                                       movie['actor_3_facebook_likes'])

movie['actor_total_facebook_likes'] = movie['actor_total_facebook_likes'].fillna(0)
```


```python
movie['pct_actor_cast_like'] = (movie['actor_total_facebook_likes'] / 
                                movie['cast_total_facebook_likes'])
```


```python
movie['pct_actor_cast_like'].min(), movie['pct_actor_cast_like'].max() 
```




    (0.0, 1.0)




```python

```


```python

```
