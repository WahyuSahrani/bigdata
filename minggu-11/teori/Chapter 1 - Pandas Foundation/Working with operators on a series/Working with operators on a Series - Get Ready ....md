

```python
import pandas as pd
import numpy as np
```


```python
movie = pd.read_csv('data/movie.csv')
imdb_score = movie['imdb_score']
imdb_score
```




    0       7.9
    1       7.1
    2       6.8
           ... 
    4913    6.3
    4914    6.3
    4915    6.6
    Name: imdb_score, Length: 4916, dtype: float64




```python
imdb_score + 1
```




    0       8.9
    1       8.1
    2       7.8
           ... 
    4913    7.3
    4914    7.3
    4915    7.6
    Name: imdb_score, Length: 4916, dtype: float64




```python
imdb_score * 2.5
```




    0       19.75
    1       17.75
    2       17.00
            ...  
    4913    15.75
    4914    15.75
    4915    16.50
    Name: imdb_score, Length: 4916, dtype: float64




```python
imdb_score // 7
```




    0       1.0
    1       1.0
    2       0.0
           ... 
    4913    0.0
    4914    0.0
    4915    0.0
    Name: imdb_score, Length: 4916, dtype: float64




```python
imdb_score > 7
```




    0        True
    1        True
    2       False
            ...  
    4913    False
    4914    False
    4915    False
    Name: imdb_score, Length: 4916, dtype: bool




```python
director = movie['director_name']
```


```python
director == 'James Cameron'
```




    0        True
    1       False
    2       False
            ...  
    4913    False
    4914    False
    4915    False
    Name: director_name, Length: 4916, dtype: bool




```python

```


```python

```


```python

```
