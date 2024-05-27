#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 


# In[3]:


data = pd.read_csv(r"C:\Users\kanch\Downloads\1. Weather Data(1).csv")


# In[1]:


data


# # How to analyze data 
# head()
# show the first (N=5) rows in the data

# In[7]:


data.head()


# .shape

# In[9]:


data.shape


# .index

# In[11]:


data.index


# .columns

# In[13]:


data.columns


# .dtypes

# In[15]:


data.dtypes


# .unique

# In[22]:


data['Weather'].unique()


# .nunique()

# In[26]:


data.nunique()


# .count

# In[27]:


data.count()


# .value_counts

# In[32]:


data['Weather'].value_counts()


# .info()

# In[33]:


data.info()


# Q. 1)  Find all the unique 'Wind Speed' values in the data.
# 
# 

# In[35]:


data.head(2)


# In[37]:


data.nunique()


# In[38]:


data['Wind Speed_km/h'].nunique()


# In[39]:


data['Wind Speed_km/h'].unique()  #answer


# Q. 2) Find the number of times when the 'Weather is exactly Clear'.

# In[6]:


data.head(2)


# In[7]:


#volue_counts()
data.Weather.value_counts()


# In[19]:


#filtering
#data.head(2)
data[data.Weather == 'Clear']


# In[24]:


#groupby()
#data.head(2)
data.groupby('Weather').get_group('Clear')


# Q. 3) Find the number of times when the 'Wind Speed was exactly 4 km/h'.

# In[25]:


data.head(2)


# In[26]:


data[data['Wind Speed_km/h'] == 4]


# Q. 4) Find out all the Null Values in the data.

# In[8]:


data.isnull()


# In[9]:


data.isnull().sum()   #answer is column


# In[10]:


data.notnull().sum()


# Q. 5) Rename the column name 'Weather' of the dataframe to 'Weather Condition'.

# In[11]:


data.head(2)


# In[15]:


data.rename(columns = {'Weather' : 'Weather Condition'}, inplace = True)  #prmanetaly


# In[36]:


data.head()


# Q. 6) What is the mean 'Visibility' ?

# In[16]:


data.head(2)


# In[17]:


data.Visibility_km.mean()


# Q. 7) What is the Standard Deviation of 'Pressure'  in this data?

# In[21]:


data.Press_kPa.std()


# Q. 8) What is the Variance of 'Relative Humidity' in this data ?

# In[22]:


data['Rel Hum_%'].var()


# Q. 9) Find all instances when 'Snow' was recorded.

# In[26]:


#value_counts()
data['Weather Condition'].value_counts()


# In[33]:


#filtering
data[data['Weather Condition'] == 'Snow'].tail(50)


# In[31]:


#str.comtains
data[data['Weather Condition'].str.contains('Snow')]


# Q. 10) Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'.

# In[34]:


data.head(2)


# In[35]:


data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]


# Q. 11) What is the Mean value of each column against each 'Weather Condition ?

# In[36]:


data.head(2)


# In[37]:


data.groupby('Weather Condition').mean()


# Q. 12) What is the Minimum & Maximum value of each column against each 'Weather Condition ?

# In[38]:


data.head(2)


# In[39]:


data.groupby('Weather Condition').min()


# In[40]:


data.groupby('Weather Condition').max()


# Q. 13) Show all the Records where Weather Condition is Fog

# In[41]:


data[data['Weather Condition'] == 'Fog']


# Q. 14) Find all instances when 'Weather is Clear' or 'Visibility is above 40'.

# In[43]:


data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40)].head(50)


# Q. 15) Find all instances when :
# A. 'Weather is Clear' and 'Relative Humidity is greater than 50'
# or
# B. 'Visibility is above 40'

# In[45]:


data[(data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50)|(data['Visibility_km'] > 40)]


# In[ ]:




