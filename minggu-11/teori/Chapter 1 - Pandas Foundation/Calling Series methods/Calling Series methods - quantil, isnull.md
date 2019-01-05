

```python
import pandas as pd
import numpy as np
```


```python
movie = pd.read_csv('data/movie.csv')
```


```python
actor_1_fb_likes.quantile(.2)
```




    510.0




```python
actor_1_fb_likes.quantile([.1, .2, .3, .4, .5, .6, .7, .8, .9])
```




    0.1      240.0
    0.2      510.0
    0.3      694.0
    0.4      854.0
            ...   
    0.6     1000.0
    0.7     8000.0
    0.8    13000.0
    0.9    18000.0
    Name: actor_1_facebook_likes, Length: 9, dtype: float64




```python
director.isnull()
```




    0       False
    1       False
    2       False
    3       False
            ...  
    4912     True
    4913    False
    4914    False
    4915    False
    Name: director_name, Length: 4916, dtype: bool




```python
actor_1_fb_likes_filled = actor_1_fb_likes.fillna(0)
actor_1_fb_likes_filled.count()
```




    4916




```python
actor_1_fb_likes_dropped = actor_1_fb_likes.dropna()
actor_1_fb_likes_dropped.size
```




    4909




```python

```


```python

```
