

```python
import pandas as pd
import numpy as np
pd.options.display.max_columns = 40
```


```python
movie = pd.read_csv('data/movie.csv', index_col='movie_title')
movie.get_dtype_counts()
```




    float64    13
    int64       3
    object     11
    dtype: int64




```python
movie.select_dtypes(include=['int']).head()
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
    </tr>
    <tr>
      <th>movie_title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Avatar</th>
    </tr>
    <tr>
      <th>Pirates of the Caribbean: At World's End</th>
    </tr>
    <tr>
      <th>Spectre</th>
    </tr>
    <tr>
      <th>The Dark Knight Rises</th>
    </tr>
    <tr>
      <th>Star Wars: Episode VII - The Force Awakens</th>
    </tr>
  </tbody>
</table>
</div>




```python
movie.select_dtypes(include=['number']).head()
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
      <th>num_critic_for_reviews</th>
      <th>duration</th>
      <th>director_facebook_likes</th>
      <th>actor_3_facebook_likes</th>
      <th>actor_1_facebook_likes</th>
      <th>gross</th>
      <th>num_voted_users</th>
      <th>cast_total_facebook_likes</th>
      <th>facenumber_in_poster</th>
      <th>num_user_for_reviews</th>
      <th>budget</th>
      <th>title_year</th>
      <th>actor_2_facebook_likes</th>
      <th>imdb_score</th>
      <th>aspect_ratio</th>
      <th>movie_facebook_likes</th>
    </tr>
    <tr>
      <th>movie_title</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Avatar</th>
      <td>723.0</td>
      <td>178.0</td>
      <td>0.0</td>
      <td>855.0</td>
      <td>1000.0</td>
      <td>760505847.0</td>
      <td>886204</td>
      <td>4834</td>
      <td>0.0</td>
      <td>3054.0</td>
      <td>237000000.0</td>
      <td>2009.0</td>
      <td>936.0</td>
      <td>7.9</td>
      <td>1.78</td>
      <td>33000</td>
    </tr>
    <tr>
      <th>Pirates of the Caribbean: At World's End</th>
      <td>302.0</td>
      <td>169.0</td>
      <td>563.0</td>
      <td>1000.0</td>
      <td>40000.0</td>
      <td>309404152.0</td>
      <td>471220</td>
      <td>48350</td>
      <td>0.0</td>
      <td>1238.0</td>
      <td>300000000.0</td>
      <td>2007.0</td>
      <td>5000.0</td>
      <td>7.1</td>
      <td>2.35</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Spectre</th>
      <td>602.0</td>
      <td>148.0</td>
      <td>0.0</td>
      <td>161.0</td>
      <td>11000.0</td>
      <td>200074175.0</td>
      <td>275868</td>
      <td>11700</td>
      <td>1.0</td>
      <td>994.0</td>
      <td>245000000.0</td>
      <td>2015.0</td>
      <td>393.0</td>
      <td>6.8</td>
      <td>2.35</td>
      <td>85000</td>
    </tr>
    <tr>
      <th>The Dark Knight Rises</th>
      <td>813.0</td>
      <td>164.0</td>
      <td>22000.0</td>
      <td>23000.0</td>
      <td>27000.0</td>
      <td>448130642.0</td>
      <td>1144337</td>
      <td>106759</td>
      <td>0.0</td>
      <td>2701.0</td>
      <td>250000000.0</td>
      <td>2012.0</td>
      <td>23000.0</td>
      <td>8.5</td>
      <td>2.35</td>
      <td>164000</td>
    </tr>
    <tr>
      <th>Star Wars: Episode VII - The Force Awakens</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>131.0</td>
      <td>NaN</td>
      <td>131.0</td>
      <td>NaN</td>
      <td>8</td>
      <td>143</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>12.0</td>
      <td>7.1</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
movie.filter(like='facebook').head()
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
      <th>director_facebook_likes</th>
      <th>actor_3_facebook_likes</th>
      <th>actor_1_facebook_likes</th>
      <th>cast_total_facebook_likes</th>
      <th>actor_2_facebook_likes</th>
      <th>movie_facebook_likes</th>
    </tr>
    <tr>
      <th>movie_title</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Avatar</th>
      <td>0.0</td>
      <td>855.0</td>
      <td>1000.0</td>
      <td>4834</td>
      <td>936.0</td>
      <td>33000</td>
    </tr>
    <tr>
      <th>Pirates of the Caribbean: At World's End</th>
      <td>563.0</td>
      <td>1000.0</td>
      <td>40000.0</td>
      <td>48350</td>
      <td>5000.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Spectre</th>
      <td>0.0</td>
      <td>161.0</td>
      <td>11000.0</td>
      <td>11700</td>
      <td>393.0</td>
      <td>85000</td>
    </tr>
    <tr>
      <th>The Dark Knight Rises</th>
      <td>22000.0</td>
      <td>23000.0</td>
      <td>27000.0</td>
      <td>106759</td>
      <td>23000.0</td>
      <td>164000</td>
    </tr>
    <tr>
      <th>Star Wars: Episode VII - The Force Awakens</th>
      <td>131.0</td>
      <td>NaN</td>
      <td>131.0</td>
      <td>143</td>
      <td>12.0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
movie.filter(regex='\d').head()
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
      <th>actor_3_facebook_likes</th>
      <th>actor_2_name</th>
      <th>actor_1_facebook_likes</th>
      <th>actor_1_name</th>
      <th>actor_3_name</th>
      <th>actor_2_facebook_likes</th>
    </tr>
    <tr>
      <th>movie_title</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Avatar</th>
      <td>855.0</td>
      <td>Joel David Moore</td>
      <td>1000.0</td>
      <td>CCH Pounder</td>
      <td>Wes Studi</td>
      <td>936.0</td>
    </tr>
    <tr>
      <th>Pirates of the Caribbean: At World's End</th>
      <td>1000.0</td>
      <td>Orlando Bloom</td>
      <td>40000.0</td>
      <td>Johnny Depp</td>
      <td>Jack Davenport</td>
      <td>5000.0</td>
    </tr>
    <tr>
      <th>Spectre</th>
      <td>161.0</td>
      <td>Rory Kinnear</td>
      <td>11000.0</td>
      <td>Christoph Waltz</td>
      <td>Stephanie Sigman</td>
      <td>393.0</td>
    </tr>
    <tr>
      <th>The Dark Knight Rises</th>
      <td>23000.0</td>
      <td>Christian Bale</td>
      <td>27000.0</td>
      <td>Tom Hardy</td>
      <td>Joseph Gordon-Levitt</td>
      <td>23000.0</td>
    </tr>
    <tr>
      <th>Star Wars: Episode VII - The Force Awakens</th>
      <td>NaN</td>
      <td>Rob Walker</td>
      <td>131.0</td>
      <td>Doug Walker</td>
      <td>NaN</td>
      <td>12.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
movie.filter(items=['actor_1_name', 'asdf']).head()
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
      <th>actor_1_name</th>
    </tr>
    <tr>
      <th>movie_title</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Avatar</th>
      <td>CCH Pounder</td>
    </tr>
    <tr>
      <th>Pirates of the Caribbean: At World's End</th>
      <td>Johnny Depp</td>
    </tr>
    <tr>
      <th>Spectre</th>
      <td>Christoph Waltz</td>
    </tr>
    <tr>
      <th>The Dark Knight Rises</th>
      <td>Tom Hardy</td>
    </tr>
    <tr>
      <th>Star Wars: Episode VII - The Force Awakens</th>
      <td>Doug Walker</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
