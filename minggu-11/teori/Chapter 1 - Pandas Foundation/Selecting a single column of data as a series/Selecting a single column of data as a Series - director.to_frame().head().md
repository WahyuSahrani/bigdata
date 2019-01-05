

```python
import pandas as pd
import numpy as np
```


```python
movie = pd.read_csv('data/movie.csv')
```


```python
director = movie['director_name'] # save Series to variable
director.name
```




    'director_name'




```python
director.to_frame().head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>director_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>James Cameron</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Gore Verbinski</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Sam Mendes</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Christopher Nolan</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Doug Walker</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
