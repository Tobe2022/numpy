#!/usr/bin/env python
# coding: utf-8

# # Mean Speed of all the Rides
# # Number of rides taken in March
# # Number of Rides where tip was more than 50 dollars
# # Number of rides where drop was JFK airport

# In[3]:


#importing the numpy Library
import numpy as np
from numpy import loadtxt


# In[4]:


#since the file has been automatically uploaded to the local host of jupyter notebook, 
#I'll download the file to jupyter notebook


# In[5]:


data = np.genfromtxt('C:\\Users\\Tobechukwu\\Downloads\\nyc_taxis.csv', delimiter =',', skip_header = 1, dtype = 'int')


# In[6]:


#since speed =d/t, 
#8th column is trip_distance. 8th column becomes 7 because counting starts from 0
#9th column is trip_lenght(in seconds). 9th becomes 8 because counting starts from 0
#9th column in seconds is converted to hour since the unit of speed will be in miles per hour (m/h)


# In[7]:


speed = data[:, 7]/ (data[:, 8]/3600)


# In[8]:


#mean speed of all rides


# In[9]:


mean_speed =speed.mean()
print(mean_speed)


# In[10]:


#number of rides taken in the month of march


# In[13]:


rides_march = data[data[:, 1] ==3,1]


# In[14]:


print(rides_march.shape[0])


# In[15]:


#number of rides where tip was more than 50 dollars = x 


# In[18]:


x= data[data[:, -3] > 50, -3].shape[0]


# In[19]:


print(x)


# In[22]:


#number of drops at JFK airport = y
#NB; drop off location corresponding to JFK airport is 6


# In[26]:


y = data[data[:, 6] == 2, 6].shape[0]


# In[27]:


print(y)


# In[ ]:




