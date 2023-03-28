#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Importing all important libraries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import scipy.stats as stats
import statsmodels.api as sm
from PIL import ImageGrab
import warnings
warnings.filterwarnings("ignore")


# In[5]:


# Reading the data
cutlets = pd.read_csv('Cutlets.csv')
cutlets


# In[6]:


# Using describe function
cutlets.describe()


# In[7]:


# Checking for any null values in data
cutlets.isnull().sum()


# In[9]:


# Checking for any duplicate values
cutlets[cutlets.duplicated()]


# In[10]:


cutlets.info()


# In[14]:


# Visualizing data
plt.subplots(figsize = (9,6))
plt.subplot(121)
plt.boxplot(cutlets['Unit A'])
plt.title('Unit A')
plt.subplot(122)
plt.boxplot(cutlets['Unit B'])
plt.title('Unit B')
plt.show()


# In[16]:


# Histogram
plt.subplots(figsize = (9,6))
plt.subplot(121)
plt.hist(cutlets['Unit A'], bins=15)
plt.title('Unit A')
plt.subplot(122)
plt.hist(cutlets['Unit B'], bins=15)
plt.title('Unit B')
plt.show()


# In[22]:


plt.figure(figsize = (8,6))
labels = ['Unit A', 'Unit B']
sns.distplot(cutlets['Unit A'], kde = True)
sns.distplot(cutlets['Unit B'],hist = True)
plt.legend(labels)


# In[23]:


sm.qqplot(cutlets['Unit A'], line='q')
plt.title('Unit A')
sm.qqplot(cutlets['Unit B'], line='q')
plt.title('Unit B')
plt.show()


# In[26]:


statistic , p_value = stats.ttest_ind(cutlets['Unit A'],cutlets['Unit B'], alternative = 'two-sided')
print('p_value=',p_value)


# In[ ]:


# As the p_value is greater than 0.05 there is significance difference between both the units

