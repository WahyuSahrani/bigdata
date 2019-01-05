

```python
import pandas as pd
import numpy as np
pd.options.display.max_columns = 40
```


```python
pd.read_csv('data/college_diversity.csv', index_col='School')
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
      <th>Diversity Index</th>
    </tr>
    <tr>
      <th>School</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Rutgers University--Newark  Newark, NJ</th>
      <td>0.76</td>
    </tr>
    <tr>
      <th>Andrews University  Berrien Springs, MI</th>
      <td>0.74</td>
    </tr>
    <tr>
      <th>Stanford University  Stanford, CA</th>
      <td>0.74</td>
    </tr>
    <tr>
      <th>University of Houston  Houston, TX</th>
      <td>0.74</td>
    </tr>
    <tr>
      <th>University of Nevada--Las Vegas  Las Vegas, NV</th>
      <td>0.74</td>
    </tr>
    <tr>
      <th>University of San Francisco  San Francisco, CA</th>
      <td>0.74</td>
    </tr>
    <tr>
      <th>San Francisco State University  San Francisco, CA</th>
      <td>0.73</td>
    </tr>
    <tr>
      <th>University of Illinois--Chicago  Chicago, IL</th>
      <td>0.73</td>
    </tr>
    <tr>
      <th>New Jersey Institute of Technology  Newark, NJ</th>
      <td>0.72</td>
    </tr>
    <tr>
      <th>Texas Woman's University  Denton, TX</th>
      <td>0.72</td>
    </tr>
  </tbody>
</table>
</div>




```python
college = pd.read_csv('data/college.csv', index_col='INSTNM')
college_ugds_ = college.filter(like='UGDS_')
college_ugds_.head()
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
      <th>UGDS_WHITE</th>
      <th>UGDS_BLACK</th>
      <th>UGDS_HISP</th>
      <th>UGDS_ASIAN</th>
      <th>UGDS_AIAN</th>
      <th>UGDS_NHPI</th>
      <th>UGDS_2MOR</th>
      <th>UGDS_NRA</th>
      <th>UGDS_UNKN</th>
    </tr>
    <tr>
      <th>INSTNM</th>
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
      <th>Alabama A &amp; M University</th>
      <td>0.0333</td>
      <td>0.9353</td>
      <td>0.0055</td>
      <td>0.0019</td>
      <td>0.0024</td>
      <td>0.0019</td>
      <td>0.0000</td>
      <td>0.0059</td>
      <td>0.0138</td>
    </tr>
    <tr>
      <th>University of Alabama at Birmingham</th>
      <td>0.5922</td>
      <td>0.2600</td>
      <td>0.0283</td>
      <td>0.0518</td>
      <td>0.0022</td>
      <td>0.0007</td>
      <td>0.0368</td>
      <td>0.0179</td>
      <td>0.0100</td>
    </tr>
    <tr>
      <th>Amridge University</th>
      <td>0.2990</td>
      <td>0.4192</td>
      <td>0.0069</td>
      <td>0.0034</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.2715</td>
    </tr>
    <tr>
      <th>University of Alabama in Huntsville</th>
      <td>0.6988</td>
      <td>0.1255</td>
      <td>0.0382</td>
      <td>0.0376</td>
      <td>0.0143</td>
      <td>0.0002</td>
      <td>0.0172</td>
      <td>0.0332</td>
      <td>0.0350</td>
    </tr>
    <tr>
      <th>Alabama State University</th>
      <td>0.0158</td>
      <td>0.9208</td>
      <td>0.0121</td>
      <td>0.0019</td>
      <td>0.0010</td>
      <td>0.0006</td>
      <td>0.0098</td>
      <td>0.0243</td>
      <td>0.0137</td>
    </tr>
  </tbody>
</table>
</div>




```python
college_ugds_.isnull().sum(axis=1).sort_values(ascending=False).head()
```




    INSTNM
    Excel Learning Center-San Antonio South         9
    Philadelphia College of Osteopathic Medicine    9
    Assemblies of God Theological Seminary          9
    Episcopal Divinity School                       9
    Phillips Graduate Institute                     9
    dtype: int64




```python
college_ugds_ = college_ugds_.dropna(how='all')
```


```python
college_ugds_.isnull().sum()
```




    UGDS_WHITE    0
    UGDS_BLACK    0
    UGDS_HISP     0
    UGDS_ASIAN    0
    UGDS_AIAN     0
    UGDS_NHPI     0
    UGDS_2MOR     0
    UGDS_NRA      0
    UGDS_UNKN     0
    dtype: int64




```python
college_ugds_.ge(.15).head()
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
      <th>UGDS_WHITE</th>
      <th>UGDS_BLACK</th>
      <th>UGDS_HISP</th>
      <th>UGDS_ASIAN</th>
      <th>UGDS_AIAN</th>
      <th>UGDS_NHPI</th>
      <th>UGDS_2MOR</th>
      <th>UGDS_NRA</th>
      <th>UGDS_UNKN</th>
    </tr>
    <tr>
      <th>INSTNM</th>
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
      <th>Alabama A &amp; M University</th>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>University of Alabama at Birmingham</th>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Amridge University</th>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>University of Alabama in Huntsville</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Alabama State University</th>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
diversity_metric = college_ugds_.ge(.15).sum(axis='columns')
diversity_metric.head()
```




    INSTNM
    Alabama A & M University               1
    University of Alabama at Birmingham    2
    Amridge University                     3
    University of Alabama in Huntsville    1
    Alabama State University               1
    dtype: int64




```python
diversity_metric.value_counts()
```




    1    3042
    2    2884
    3     876
    4      63
    0       7
    5       2
    dtype: int64




```python
diversity_metric.sort_values(ascending=False).head()
```




    INSTNM
    Regency Beauty Institute-Austin          5
    Central Texas Beauty College-Temple      5
    Sullivan and Cogliano Training Center    4
    Ambria College of Nursing                4
    Berkeley College-New York                4
    dtype: int64




```python
college_ugds_.loc[['Regency Beauty Institute-Austin', 
                          'Central Texas Beauty College-Temple']]
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
      <th>UGDS_WHITE</th>
      <th>UGDS_BLACK</th>
      <th>UGDS_HISP</th>
      <th>UGDS_ASIAN</th>
      <th>UGDS_AIAN</th>
      <th>UGDS_NHPI</th>
      <th>UGDS_2MOR</th>
      <th>UGDS_NRA</th>
      <th>UGDS_UNKN</th>
    </tr>
    <tr>
      <th>INSTNM</th>
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
      <th>Regency Beauty Institute-Austin</th>
      <td>0.1867</td>
      <td>0.2133</td>
      <td>0.1600</td>
      <td>0.0000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.1733</td>
      <td>0.0</td>
      <td>0.2667</td>
    </tr>
    <tr>
      <th>Central Texas Beauty College-Temple</th>
      <td>0.1616</td>
      <td>0.2323</td>
      <td>0.2626</td>
      <td>0.0202</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.1717</td>
      <td>0.0</td>
      <td>0.1515</td>
    </tr>
  </tbody>
</table>
</div>




```python
us_news_top = ['Rutgers University-Newark', 
               'Andrews University', 
               'Stanford University', 
               'University of Houston',
               'University of Nevada-Las Vegas']
```


```python
diversity_metric.loc[us_news_top]
```




    INSTNM
    Rutgers University-Newark         4
    Andrews University                3
    Stanford University               3
    University of Houston             3
    University of Nevada-Las Vegas    3
    dtype: int64




```python
college_ugds_.max(axis=1).sort_values(ascending=False).head(10)
```




    INSTNM
    Dewey University-Manati                               1.0
    Yeshiva and Kollel Harbotzas Torah                    1.0
    Mr Leon's School of Hair Design-Lewiston              1.0
    Dewey University-Bayamon                              1.0
    Shepherds Theological Seminary                        1.0
    Yeshiva Gedolah Kesser Torah                          1.0
    Monteclaro Escuela de Hoteleria y Artes Culinarias    1.0
    Yeshiva Shaar Hatorah                                 1.0
    Bais Medrash Elyon                                    1.0
    Yeshiva of Nitra Rabbinical College                   1.0
    dtype: float64




```python
college_ugds_.loc['Talmudical Seminary Oholei Torah']
```




    UGDS_WHITE    1.0
    UGDS_BLACK    0.0
    UGDS_HISP     0.0
    UGDS_ASIAN    0.0
    UGDS_AIAN     0.0
    UGDS_NHPI     0.0
    UGDS_2MOR     0.0
    UGDS_NRA      0.0
    UGDS_UNKN     0.0
    Name: Talmudical Seminary Oholei Torah, dtype: float64




```python
(college_ugds_ > .01).all(axis=1).any()
```




    True




```python

```
