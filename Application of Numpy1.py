#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Applying Numpy to Data Solutions

# Mean Speed of all the Rides
# Number of rides taken in March
# Number of Rides where tip was more than 50 dollars
# Number of rides where drop was JFK airport


# In[2]:


#importing the numpy Library
import numpy as np


# In[6]:


#since the file has been automatically uploaded to the local host of jupyter notebook, 
#I'll download the file to jupyter notebook

data = np.genfromtxt('C:\\Users\\Tobechukwu\\Downloads\\nyc_taxis.csv', delimiter =',', skip_header = 1, dtype = 'int')


# In[7]:


#since speed =d/t, 
#8th column is trip_distance. 8th column becomes 7 because counting starts from 0
#9th column is trip_lenght(in seconds). 9th becomes 8 because counting starts from 0
#9th column in seconds is converted to hour since the unit of speed will be in miles per hour (m/h)

speed = data[:, 7]/ (data[:, 8]/3600)

#mean speed of all rides

mean_speed =speed.mean()
print(mean_speed)


# In[8]:


#number of rides taken in the month of march

rides_march = data[data[:, 1] ==3,1]
print(rides_march.shape[0])


# In[9]:


#number of rides where tip was more than 50 dollars = x 

x= data[data[:, -3] > 50, -3].shape[0]
print(x)


# In[10]:


#number of drops at JFK airport = y
#NB; drop off location corresponding to JFK airport is 6

y = data[data[:, 6] == 2, 6].shape[0]
print(y)


# In[ ]:




