

```python
import pandas as pd
import numpy as np
pd.options.display.max_columns = 40
```


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
college_ugds_.count()
```




    UGDS_WHITE    6874
    UGDS_BLACK    6874
    UGDS_HISP     6874
    UGDS_ASIAN    6874
    UGDS_AIAN     6874
    UGDS_NHPI     6874
    UGDS_2MOR     6874
    UGDS_NRA      6874
    UGDS_UNKN     6874
    dtype: int64




```python
college_ugds_.count(axis=0)
```




    UGDS_WHITE    6874
    UGDS_BLACK    6874
    UGDS_HISP     6874
    UGDS_ASIAN    6874
    UGDS_AIAN     6874
    UGDS_NHPI     6874
    UGDS_2MOR     6874
    UGDS_NRA      6874
    UGDS_UNKN     6874
    dtype: int64




```python
college_ugds_.count(axis='index')
```




    UGDS_WHITE    6874
    UGDS_BLACK    6874
    UGDS_HISP     6874
    UGDS_ASIAN    6874
    UGDS_AIAN     6874
    UGDS_NHPI     6874
    UGDS_2MOR     6874
    UGDS_NRA      6874
    UGDS_UNKN     6874
    dtype: int64




```python
college_ugds_.count(axis='columns').head()
```




    INSTNM
    Alabama A & M University               9
    University of Alabama at Birmingham    9
    Amridge University                     9
    University of Alabama in Huntsville    9
    Alabama State University               9
    dtype: int64




```python
college_ugds_.median(axis='index')
```




    UGDS_WHITE    0.55570
    UGDS_BLACK    0.10005
    UGDS_HISP     0.07140
    UGDS_ASIAN    0.01290
    UGDS_AIAN     0.00260
    UGDS_NHPI     0.00000
    UGDS_2MOR     0.01750
    UGDS_NRA      0.00000
    UGDS_UNKN     0.01430
    dtype: float64




```python
college_ugds_cumsum = college_ugds_.cumsum(axis=1)
college_ugds_cumsum.head()
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
      <td>0.9686</td>
      <td>0.9741</td>
      <td>0.9760</td>
      <td>0.9784</td>
      <td>0.9803</td>
      <td>0.9803</td>
      <td>0.9862</td>
      <td>1.0000</td>
    </tr>
    <tr>
      <th>University of Alabama at Birmingham</th>
      <td>0.5922</td>
      <td>0.8522</td>
      <td>0.8805</td>
      <td>0.9323</td>
      <td>0.9345</td>
      <td>0.9352</td>
      <td>0.9720</td>
      <td>0.9899</td>
      <td>0.9999</td>
    </tr>
    <tr>
      <th>Amridge University</th>
      <td>0.2990</td>
      <td>0.7182</td>
      <td>0.7251</td>
      <td>0.7285</td>
      <td>0.7285</td>
      <td>0.7285</td>
      <td>0.7285</td>
      <td>0.7285</td>
      <td>1.0000</td>
    </tr>
    <tr>
      <th>University of Alabama in Huntsville</th>
      <td>0.6988</td>
      <td>0.8243</td>
      <td>0.8625</td>
      <td>0.9001</td>
      <td>0.9144</td>
      <td>0.9146</td>
      <td>0.9318</td>
      <td>0.9650</td>
      <td>1.0000</td>
    </tr>
    <tr>
      <th>Alabama State University</th>
      <td>0.0158</td>
      <td>0.9366</td>
      <td>0.9487</td>
      <td>0.9506</td>
      <td>0.9516</td>
      <td>0.9522</td>
      <td>0.9620</td>
      <td>0.9863</td>
      <td>1.0000</td>
    </tr>
  </tbody>
</table>
</div>




```python
college_ugds_cumsum.sort_values('UGDS_HISP', ascending=False)
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
      <th>New Beginning College of Cosmetology</th>
      <td>0.8957</td>
      <td>0.9305</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>Virginia University of Lynchburg</th>
      <td>0.0120</td>
      <td>0.9921</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>Turning Point Beauty College</th>
      <td>0.1915</td>
      <td>0.2341</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>First Coast Barber Academy</th>
      <td>0.1667</td>
      <td>0.9445</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>Poplar Bluff Technical Career Center</th>
      <td>0.9362</td>
      <td>0.9788</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>CDE Career Institute</th>
      <td>0.6452</td>
      <td>0.9033</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>La'James International College</th>
      <td>0.7917</td>
      <td>0.8334</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>Academy of Esthetics and Cosmetology</th>
      <td>0.0556</td>
      <td>0.0834</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>D &amp; L Academy of Hair Design</th>
      <td>0.6667</td>
      <td>0.7084</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>Educators of Beauty College of Cosmetology-Sterling</th>
      <td>0.8605</td>
      <td>0.9303</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>Independence College of Cosmetology</th>
      <td>0.8511</td>
      <td>0.9575</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>First Class Cosmetology School</th>
      <td>0.4744</td>
      <td>0.8847</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>Sidneys Hair Dressing College</th>
      <td>0.9063</td>
      <td>0.9376</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>Business Informatics Center Inc</th>
      <td>0.5417</td>
      <td>0.8334</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>ASI Career Institute</th>
      <td>0.6147</td>
      <td>0.8808</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>Salon Academy</th>
      <td>0.8267</td>
      <td>0.9734</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>Tiffin Academy of Hair Design</th>
      <td>0.8929</td>
      <td>0.9465</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>Management Resources College</th>
      <td>0.0071</td>
      <td>0.0594</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>Gemini School of Visual Arts &amp; Communication</th>
      <td>0.7143</td>
      <td>0.8572</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>NeeCee's College of Cosmetology</th>
      <td>0.3810</td>
      <td>0.7620</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>Choffin Career  and Technical Center</th>
      <td>0.6063</td>
      <td>0.9688</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>Laredo Beauty College Inc</th>
      <td>0.0068</td>
      <td>0.0136</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>Venango County Area Vocational Technical School</th>
      <td>0.9688</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>Metro Business College-Arnold</th>
      <td>0.8889</td>
      <td>0.9445</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>SABER College</th>
      <td>0.0017</td>
      <td>0.0884</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>Toledo Restaurant Training Center</th>
      <td>0.3226</td>
      <td>0.9678</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>Elite Welding Academy LLC</th>
      <td>0.9455</td>
      <td>0.9819</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>Aesthetic Science Institute</th>
      <td>0.9697</td>
      <td>0.9849</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>Ashtabula County Technical and Career Campus</th>
      <td>0.9385</td>
      <td>0.9847</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>Healthcare Training Institute</th>
      <td>0.1974</td>
      <td>0.7106</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Strayer University-Lawrenceville</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Piscataway</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Utah County Campus</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>L'esprit Academy - Royal Oak</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>National Career Institute - Jersey City Branch</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Cobb Campus</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Morrow Campus</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Roswell Campus</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Douglasville Campus</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Lithonia Campus</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Savannah Campus</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Augusta Campus</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Columbus</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Columbia Campus</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Charleston Campus</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Irving</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Katy</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Northwest Houston</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Plano</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Cedar Hill</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-North Dallas</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-San Antonio</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Stafford</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>WestMed College - Merced</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Vantage College</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>SAE Institute of Technology  San Francisco</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Rasmussen College - Overland Park</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>National Personal Training Institute of Cleveland</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Bay Area Medical Academy - San Jose Satellite Location</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Excel Learning Center-San Antonio South</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>7535 rows × 9 columns</p>
</div>




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
