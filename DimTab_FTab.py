#!/usr/bin/env python
# coding: utf-8

# In[10]:


get_ipython().system('pip install seaborn')


# In[11]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import warnings
warnings.filterwarnings("ignore")


# In[13]:


df = pd.read_csv('dataset.csv')


# In[14]:


df.head(5)


# In[15]:


print(df.shape)


# In[16]:


df.dtypes


# In[17]:


df['Order Date'] = pd.to_datetime(df['Order Date'])
# alternative
df['Order Date'].astype('datetime64[ns]')


# In[18]:


df.dtypes


# In[19]:


df['Order Date'].head()


# In[20]:


df['Quarter'] = df['Order Date'].apply(lambda x: x.quarter)
df['Year'] = df['Order Date'].apply(lambda x: x.year)
df['Month'] = df['Order Date'].apply(lambda x: x.month)
df['Week'] = df['Order Date'].apply(lambda x: x.week)
df['Day'] = df['Order Date'].apply(lambda x: x.day)


# In[21]:


df.head()


# In[22]:


df.dtypes


# In[23]:


# sirf date ko bahir nikala
dimDate = df[['Order Date']]
dimDate.head()


# In[24]:


# number of records
dimDate.shape[0]


# In[25]:


# upar datewise repiiton hai tabhi 8399 records hain
# ab total unique records 1418 hain

dimDate['Order Date'].nunique()


# In[26]:


# remove duplications
dimDate = dimDate.drop_duplicates()
dimDate.shape[0]


# In[27]:


# date m 5 columns add kardiye
dimDate['Quarter'] = dimDate['Order Date'].apply(lambda x: x.quarter)
dimDate['Year'] = dimDate['Order Date'].apply(lambda x: x.year)
dimDate['Month'] = dimDate['Order Date'].apply(lambda x: x.month)
dimDate['Week'] = dimDate['Order Date'].apply(lambda x: x.week)
dimDate['Day'] = dimDate['Order Date'].apply(lambda x: x.day)

dimDate.head(10)


# In[28]:


# uko utha k sort bhi kardia
dimDate = dimDate.sort_values(by='Order Date')
dimDate.head(10)


# In[ ]:





# In[29]:


dimDate.to_csv('DimDate.csv', index= False)


# In[31]:


dimDf=pd.read_csv("DimDate.csv")


# In[32]:


dimDf.head()


# In[ ]:





# In[ ]:




