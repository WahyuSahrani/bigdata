

```python
import pandas as pd
import numpy as np
```


```python
movie = pd.read_csv('data/movie.csv')
actor_1_fb_likes = movie['actor_1_facebook_likes']
director = movie['director_name']
```


```python
director.value_counts().head(3)
```




    Steven Spielberg    26
    Woody Allen         22
    Martin Scorsese     20
    Name: director_name, dtype: int64




```python
actor_1_fb_likes.isnull().sum()
```




    7




```python
actor_1_fb_likes.dtype
```




    dtype('float64')




```python
actor_1_fb_likes.fillna(0)\
                .astype(int)\
                .head()
```




    0     1000
    1    40000
    2    11000
    3    27000
    4      131
    Name: actor_1_facebook_likes, dtype: int32




```python

```


```python


```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```
