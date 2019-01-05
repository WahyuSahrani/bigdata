

```python
import pandas as pd
import numpy as np
```


```python
movie = pd.read_csv('data/movie.csv')
```


```python
actor_1_fb_likes.min(), actor_1_fb_likes.max(), \
actor_1_fb_likes.mean(), actor_1_fb_likes.median(), \
actor_1_fb_likes.std(), actor_1_fb_likes.sum()
```




    (0.0, 640000.0, 6494.488490527602, 982.0, 15106.986883848309, 31881444.0)




```python
actor_1_fb_likes.describe()
```




    count      4909.000000
    mean       6494.488491
    std       15106.986884
    min           0.000000
    25%         607.000000
    50%         982.000000
    75%       11000.000000
    max      640000.000000
    Name: actor_1_facebook_likes, dtype: float64




```python
director.describe()
```




    count                 4814
    unique                2397
    top       Steven Spielberg
    freq                    26
    Name: director_name, dtype: object




```python

```


```python

```


```python

```


```python

```
