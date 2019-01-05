

```python
import pandas as pd
import numpy as np
```


```python
imdb_score.add(1)              # imdb_score + 1
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
imdb_score.mul(2.5)            # imdb_score * 2.5
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
imdb_score.floordiv(7)         # imdb_score // 7
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
imdb_score.gt(7)               # imdb_score > 7
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
director.eq('James Cameron')   # director == 'James Cameron'
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
director = movie['director_name']
```


```python
director.eq('James Cameron')   # director == 'James Cameron'
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
imdb_score.astype(int).mod(5)
```




    0       2
    1       2
    2       1
           ..
    4913    1
    4914    1
    4915    1
    Name: imdb_score, Length: 4916, dtype: int32




```python
a = type(1)
```


```python
type(a)
```




    type




```python
a = type(imdb_score)
```


```python
a([1,2,3])
```




    0    1
    1    2
    2    3
    dtype: int64




```python

```
