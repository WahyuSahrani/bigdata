

```python
import pandas as pd
import numpy as np
pd.options.display.max_columns = 40
```


```python
movie = pd.read_csv('data/movie.csv')
movie[['color', 'movie_title', 'color']].max()
```




    Series([], dtype: float64)




```python
movie.select_dtypes(['object']).fillna('').max()
```




    color                                                          Color
    director_name                                          Étienne Faure
    actor_2_name                                           Zubaida Sahar
    genres                                                       Western
    actor_1_name                                           Óscar Jaenada
    movie_title                                                 Æon Flux
    actor_3_name                                           Óscar Jaenada
    plot_keywords                                    zombie|zombie spoof
    movie_imdb_link    http://www.imdb.com/title/tt5574490/?ref_=fn_t...
    language                                                        Zulu
    country                                                 West Germany
    content_rating                                                     X
    dtype: object




```python

```


```python

```


```python

```
