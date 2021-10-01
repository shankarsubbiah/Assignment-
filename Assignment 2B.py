#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df=pd.read_csv(r"C:\Users\Prima\OneDrive\Documents\college_1.csv")
df1=pd.read_csv(r"C:\Users\Prima\OneDrive\Documents\college_2.csv")
df2=pd.merge(df,df1, how='outer')
df2.info()


# In[8]:


df3=df2.drop(['python','mysql','Department','Rising', 'python_en', 'computational_thinking','Previous Geekions'],axis='columns')
df3.head()


# In[9]:


df4=df3[df3['CodeKata Score']>15000]
df4.to_csv('Exceeded expectations.csv')
df4.head()


# In[10]:


df5=df3[df3['CodeKata Score'].between(10000,15000)]
df5.to_csv('Reached_expectations.csv')
df5.head()


# In[11]:


df6=df3[df3['CodeKata Score'].between(7000,10000)]
df6.to_csv('Needs_Improvement.csv')
df6.head()


# In[12]:


df7=df3[df3['CodeKata Score']<7000]
df7.to_csv('Unsatisfactory.csv')
df7.head()


# In[13]:


df2.head()


# In[18]:


mean_pg=df2['Previous Geekions'].mean()
mean_ck=df2['CodeKata Score'].mean()
print(mean_pg)
print(mean_ck)


# In[20]:


df8=df3['Name'].count()
print(df8)


# In[21]:


mean_py=df2['python'].mean()
mean_mysql=df2['mysql'].mean()
mean_py_E=df2['python_en'].mean()
mean_ct=df2['computational_thinking'].mean()
print(mean_py)
print(mean_mysql)
print(mean_py_E)
print(mean_ct)


# In[22]:


df2.nlargest(3,['Rising'])


# In[24]:


df2.nlargest(3,['Previous Geekions'])


# In[25]:


import matplotlib.pyplot as plt
(df2['Department'].value_counts()).plot.pie()


# In[26]:


import seaborn as sns
sns.countplot(df2['Department'])


# In[ ]:




