#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


df = pd.read_csv('homeprice.csv')
df


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.xlabel('area')
plt.ylabel('price')
plt.grid()
plt.scatter(df.area, df.price, color = 'blue', marker = '*')


# In[4]:


new_df = df.drop('price', axis = "columns")
new_df


# In[5]:


price = df.price
print(type(price))
np.array(price)


# In[6]:


#create linear regression object
reg = linear_model.LinearRegression()
reg.fit(new_df, price)


# In[7]:


reg.predict([[4500]])


# In[8]:


reg.coef_ #value of m slope


# In[9]:


reg.intercept_ #value of intercept c


# In[10]:


area_df = pd.read_csv('area.csv')
area_df.head()


# In[11]:


p = reg.predict(area_df)
p


# In[12]:


area_df['predicted_prices'] = p
area_df


# In[13]:


area_df.to_csv('prediction.csv')


# In[14]:


from sklearn.metrics import accuracy_score


# In[ ]:




