

```python
import pandas as pd
import numpy as np
pd.options.display.max_columns = 40
```


```python
pd.options.display.max_rows = 8
movie = pd.read_csv('data/movie.csv')
movie.shape
```




    (4916, 28)




```python
movie.size
```




    137648




```python
movie.ndim

```




    2




```python
len(movie)
```




    4916




```python
movie.count()
```




    color                     4897
    director_name             4814
    num_critic_for_reviews    4867
    duration                  4901
                              ... 
    actor_2_facebook_likes    4903
    imdb_score                4916
    aspect_ratio              4590
    movie_facebook_likes      4916
    Length: 28, dtype: int64




```python
movie.min()
```




    num_critic_for_reviews     1.00
    duration                   7.00
    director_facebook_likes    0.00
    actor_3_facebook_likes     0.00
                               ... 
    actor_2_facebook_likes     0.00
    imdb_score                 1.60
    aspect_ratio               1.18
    movie_facebook_likes       0.00
    Length: 16, dtype: float64




```python
movie2 = movie[new_col_order]
movie2.head()
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
      <th>movie_title</th>
      <th>title_year</th>
      <th>content_rating</th>
      <th>genres</th>
      <th>director_name</th>
      <th>actor_1_name</th>
      <th>actor_2_name</th>
      <th>actor_3_name</th>
      <th>color</th>
      <th>country</th>
      <th>language</th>
      <th>plot_keywords</th>
      <th>movie_imdb_link</th>
      <th>director_facebook_likes</th>
      <th>actor_1_facebook_likes</th>
      <th>actor_2_facebook_likes</th>
      <th>actor_3_facebook_likes</th>
      <th>cast_total_facebook_likes</th>
      <th>movie_facebook_likes</th>
      <th>budget</th>
      <th>gross</th>
      <th>num_voted_users</th>
      <th>num_user_for_reviews</th>
      <th>num_critic_for_reviews</th>
      <th>imdb_score</th>
      <th>duration</th>
      <th>aspect_ratio</th>
      <th>facenumber_in_poster</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Avatar</td>
      <td>2009.0</td>
      <td>PG-13</td>
      <td>Action|Adventure|Fantasy|Sci-Fi</td>
      <td>James Cameron</td>
      <td>CCH Pounder</td>
      <td>Joel David Moore</td>
      <td>Wes Studi</td>
      <td>Color</td>
      <td>USA</td>
      <td>English</td>
      <td>avatar|future|marine|native|paraplegic</td>
      <td>http://www.imdb.com/title/tt0499549/?ref_=fn_t...</td>
      <td>0.0</td>
      <td>1000.0</td>
      <td>936.0</td>
      <td>855.0</td>
      <td>4834</td>
      <td>33000</td>
      <td>237000000.0</td>
      <td>760505847.0</td>
      <td>886204</td>
      <td>3054.0</td>
      <td>723.0</td>
      <td>7.9</td>
      <td>178.0</td>
      <td>1.78</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Pirates of the Caribbean: At World's End</td>
      <td>2007.0</td>
      <td>PG-13</td>
      <td>Action|Adventure|Fantasy</td>
      <td>Gore Verbinski</td>
      <td>Johnny Depp</td>
      <td>Orlando Bloom</td>
      <td>Jack Davenport</td>
      <td>Color</td>
      <td>USA</td>
      <td>English</td>
      <td>goddess|marriage ceremony|marriage proposal|pi...</td>
      <td>http://www.imdb.com/title/tt0449088/?ref_=fn_t...</td>
      <td>563.0</td>
      <td>40000.0</td>
      <td>5000.0</td>
      <td>1000.0</td>
      <td>48350</td>
      <td>0</td>
      <td>300000000.0</td>
      <td>309404152.0</td>
      <td>471220</td>
      <td>1238.0</td>
      <td>302.0</td>
      <td>7.1</td>
      <td>169.0</td>
      <td>2.35</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Spectre</td>
      <td>2015.0</td>
      <td>PG-13</td>
      <td>Action|Adventure|Thriller</td>
      <td>Sam Mendes</td>
      <td>Christoph Waltz</td>
      <td>Rory Kinnear</td>
      <td>Stephanie Sigman</td>
      <td>Color</td>
      <td>UK</td>
      <td>English</td>
      <td>bomb|espionage|sequel|spy|terrorist</td>
      <td>http://www.imdb.com/title/tt2379713/?ref_=fn_t...</td>
      <td>0.0</td>
      <td>11000.0</td>
      <td>393.0</td>
      <td>161.0</td>
      <td>11700</td>
      <td>85000</td>
      <td>245000000.0</td>
      <td>200074175.0</td>
      <td>275868</td>
      <td>994.0</td>
      <td>602.0</td>
      <td>6.8</td>
      <td>148.0</td>
      <td>2.35</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>The Dark Knight Rises</td>
      <td>2012.0</td>
      <td>PG-13</td>
      <td>Action|Thriller</td>
      <td>Christopher Nolan</td>
      <td>Tom Hardy</td>
      <td>Christian Bale</td>
      <td>Joseph Gordon-Levitt</td>
      <td>Color</td>
      <td>USA</td>
      <td>English</td>
      <td>deception|imprisonment|lawlessness|police offi...</td>
      <td>http://www.imdb.com/title/tt1345836/?ref_=fn_t...</td>
      <td>22000.0</td>
      <td>27000.0</td>
      <td>23000.0</td>
      <td>23000.0</td>
      <td>106759</td>
      <td>164000</td>
      <td>250000000.0</td>
      <td>448130642.0</td>
      <td>1144337</td>
      <td>2701.0</td>
      <td>813.0</td>
      <td>8.5</td>
      <td>164.0</td>
      <td>2.35</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Star Wars: Episode VII - The Force Awakens</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Documentary</td>
      <td>Doug Walker</td>
      <td>Doug Walker</td>
      <td>Rob Walker</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>http://www.imdb.com/title/tt5289954/?ref_=fn_t...</td>
      <td>131.0</td>
      <td>131.0</td>
      <td>12.0</td>
      <td>NaN</td>
      <td>143</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7.1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
movie.describe()
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
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>4867.000000</td>
      <td>4901.000000</td>
      <td>4814.000000</td>
      <td>4893.000000</td>
      <td>4909.000000</td>
      <td>4.054000e+03</td>
      <td>4.916000e+03</td>
      <td>4916.000000</td>
      <td>4903.000000</td>
      <td>4895.000000</td>
      <td>4.432000e+03</td>
      <td>4810.000000</td>
      <td>4903.000000</td>
      <td>4916.000000</td>
      <td>4590.000000</td>
      <td>4916.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>137.988905</td>
      <td>107.090798</td>
      <td>691.014541</td>
      <td>631.276313</td>
      <td>6494.488491</td>
      <td>4.764451e+07</td>
      <td>8.264492e+04</td>
      <td>9579.815907</td>
      <td>1.377320</td>
      <td>267.668846</td>
      <td>3.654749e+07</td>
      <td>2002.447609</td>
      <td>1621.923516</td>
      <td>6.437429</td>
      <td>2.222349</td>
      <td>7348.294142</td>
    </tr>
    <tr>
      <th>std</th>
      <td>120.239379</td>
      <td>25.286015</td>
      <td>2832.954125</td>
      <td>1625.874802</td>
      <td>15106.986884</td>
      <td>6.737255e+07</td>
      <td>1.383222e+05</td>
      <td>18164.316990</td>
      <td>2.023826</td>
      <td>372.934839</td>
      <td>1.002427e+08</td>
      <td>12.453977</td>
      <td>4011.299523</td>
      <td>1.127802</td>
      <td>1.402940</td>
      <td>19206.016458</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>7.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.620000e+02</td>
      <td>5.000000e+00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>2.180000e+02</td>
      <td>1916.000000</td>
      <td>0.000000</td>
      <td>1.600000</td>
      <td>1.180000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>49.000000</td>
      <td>93.000000</td>
      <td>7.000000</td>
      <td>132.000000</td>
      <td>607.000000</td>
      <td>5.019656e+06</td>
      <td>8.361750e+03</td>
      <td>1394.750000</td>
      <td>0.000000</td>
      <td>64.000000</td>
      <td>6.000000e+06</td>
      <td>1999.000000</td>
      <td>277.000000</td>
      <td>5.800000</td>
      <td>1.850000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>108.000000</td>
      <td>103.000000</td>
      <td>48.000000</td>
      <td>366.000000</td>
      <td>982.000000</td>
      <td>2.504396e+07</td>
      <td>3.313250e+04</td>
      <td>3049.000000</td>
      <td>1.000000</td>
      <td>153.000000</td>
      <td>1.985000e+07</td>
      <td>2005.000000</td>
      <td>593.000000</td>
      <td>6.600000</td>
      <td>2.350000</td>
      <td>159.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>191.000000</td>
      <td>118.000000</td>
      <td>189.750000</td>
      <td>633.000000</td>
      <td>11000.000000</td>
      <td>6.110841e+07</td>
      <td>9.377275e+04</td>
      <td>13616.750000</td>
      <td>2.000000</td>
      <td>320.500000</td>
      <td>4.300000e+07</td>
      <td>2011.000000</td>
      <td>912.000000</td>
      <td>7.200000</td>
      <td>2.350000</td>
      <td>2000.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>813.000000</td>
      <td>511.000000</td>
      <td>23000.000000</td>
      <td>23000.000000</td>
      <td>640000.000000</td>
      <td>7.605058e+08</td>
      <td>1.689764e+06</td>
      <td>656730.000000</td>
      <td>43.000000</td>
      <td>5060.000000</td>
      <td>4.200000e+09</td>
      <td>2016.000000</td>
      <td>137000.000000</td>
      <td>9.500000</td>
      <td>16.000000</td>
      <td>349000.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.options.display.max_rows = 8
```


```python
movie.isnull().sum()
```




    color                      19
    director_name             102
    num_critic_for_reviews     49
    duration                   15
                             ... 
    actor_2_facebook_likes     13
    imdb_score                  0
    aspect_ratio              326
    movie_facebook_likes        0
    Length: 28, dtype: int64




```python
movie.min(skipna=False)
```

    C:\Users\wahyu\Anaconda3\lib\site-packages\numpy\core\_methods.py:32: RuntimeWarning: invalid value encountered in reduce
      return umr_minimum(a, axis, None, out, keepdims, initial)
    




    num_critic_for_reviews     NaN
    duration                   NaN
    director_facebook_likes    NaN
    actor_3_facebook_likes     NaN
                              ... 
    actor_2_facebook_likes     NaN
    imdb_score                 1.6
    aspect_ratio               NaN
    movie_facebook_likes       0.0
    Length: 16, dtype: float64




```python

```
