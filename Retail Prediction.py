#!/usr/bin/env python
# coding: utf-8

# # The Sparks Foundation
# # GRIPMAY21
# # Mukesh Sahu
# # Project:- Exploratory Data Analysis - Retail
# 
# 
# **.Perform ‘Exploratory Data Analysis’ on dataset ‘SampleSuperstore’ 
# .As a business manager, try to find out the weak areas where you can 
# work to make more profit.**
# 

# In[4]:


# Load the required libraries for analysis of data
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


# Set working directory
os.chdir("Downloads")


# In[6]:


# lets Check working directory
os.getcwd()


# In[7]:


# Load the data
Retail_Data = pd.read_csv("retail.csv")


# In[8]:


Retail_Data.head()


# In[9]:


Retail_Data.tail()


# In[10]:


Retail_Data.shape


# In[11]:


Retail_Data.columns


# In[12]:


Retail_Data.dtypes


# In[13]:


# dipects the data types and null values 
Retail_Data.info()


# In[14]:


# lets Check summary of the dataset 
Retail_Data.describe()


# In[15]:


# Missing Value anlysis

# to check if there is any missing values
Missing_val = Retail_Data.isnull().sum()
Missing_val
# In our dataset we dont have any missing values.so that we dont need to do any imputation methods 


# In[49]:



# Continous Variables 
cnames= [ 'Quantity', 'Discount']


# In[56]:


# Outlier Analysis

# Lets save copy of dataset before preprocessing
df = Retail_Data.copy()
Retail_Data = df.copy() 

# Using seaborn library, we can viualize the outliers by plotting box plot

fig, ax= plt.subplots(1, 2, figsize=(12,8))
sns.boxplot(x=df["Discount"], ax=ax[0])
sns.boxplot(x=df["Quantity"], ax=ax[1])
    


# In[57]:


Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
df_new=df[~((df<(Q1-1.5*IQR))|(df>(Q3+1.5*IQR))).any(axis=1)]


# In[58]:


#new shape
df_new.shape


# In[59]:


#After removing the Outliers
for i in cnames:
    print(i)
    sns.boxplot(y=df_new[i])
    plt.xlabel(i)
    plt.ylabel("values")
    plt.title("Boxplot of "+i)
    plt.show()
    


# In[64]:


df=df_new.copy()


# In[65]:


df.head()


# In[66]:


# check for duplicates
df.duplicated().sum()


# In[67]:


# Drop duplicated values 
df.drop_duplicates(inplace =True)


# In[68]:


# NO diuplicates available. 
df.duplicated().sum()


# In[69]:


# Drop the unnecessary columns. We can drop postal code since it does not have any inmpact sales and profit. 
df.drop(columns= "Postal Code", axis=1, inplace=True)


# In[70]:


df.head()


# In[71]:


corel = df.corr()
corel


# In[72]:


# Heatmap for colinearity between the Sales,profit, quantity and discount. 
sns.heatmap(corel, annot=True)


# In[73]:


# State group wise view numerical data as a mean value
df_state=df.groupby(['State'])[['Quantity','Sales','Discount','Profit']].mean()
df_state


# In[74]:


# State group wise view numerical data as a min value
df_state=df.groupby(['State'])[['Quantity','Sales','Discount','Profit']].min()
df_state


# In[75]:


df_state=df.groupby(['State'])[['Quantity','Sales','Discount','Profit']].max()
df_state


# In[76]:


# State group wise view numerical data as a median value
df_state=df.groupby(['State'])[['Quantity','Sales','Discount','Profit']].median()
df_state


# In[77]:


sales_profit = df.groupby('State')['Profit'].sum()
plt.figure(figsize=(18,6))
sns.barplot(x=sales_profit.index, y=sales_profit.values)
plt.xticks(rotation=90)
plt.ylabel('Profit')
plt.show()


# In[78]:


sns.pairplot(df, hue='Region', diag_kind="hist")


# In[81]:


sns.pairplot(df,hue='Category')


# In[82]:


sns.pairplot(df,hue='Segment')


# In[83]:


sns.countplot("Ship Mode",data=df)


# In[84]:


sns.countplot("Segment",data=df)


# In[85]:


sns.countplot("Region",data=df)


# In[86]:


sns.countplot("Category",data=df)


# In[87]:


sales = df.groupby('State')['Sales'].sum().sort_values(ascending=False)
sales[:10].plot(kind ='bar') # sales of top 10 states


# In[88]:


states = df.groupby('State')['Sales'].sum()
states.sort_values(ascending=False, inplace=True)
fig, ax=plt.subplots(figsize=(20,10))
plt.title("States with sales", size=30)
states.plot.bar()


# In[89]:


profit=df[df.Profit>0]
loss=df[df.Profit<0]

# percentage share of total profit by each sub-category
plt.pie(profit.groupby('Sub-Category').agg('sum').Profit,radius=3.12,labels=profit.groupby('Sub-Category').agg('sum').index,
       autopct='%1.2f%%')
plt.title('Profit pie',fontdict=dict(fontsize=36),pad=100,loc='center')
plt.show()


# In[ ]:





# In[91]:


# Sales profit per category
category = df.groupby(['Sub-Category'])['Profit','Sales'].sum()
category.plot.bar(rot=2,figsize=(20,10))


# In[92]:


pd.crosstab( df['Region'],df['Category']).plot(kind='bar', figsize=(18,5))
plt.xticks(rotation=45)
plt.plot()


# In[93]:


# To see the Region wise different sub-categories order
plt.figure(figsize=(10,6))
sns.countplot(x="Sub-Category", hue="Region",data=df)
plt.xticks(rotation="vertical")
plt.show()


# **Conclusions :-**
# 
# **Here we observe that there is a moderate positive correlation between "Sales" and "Profit".
# On the other hand, there is a negative correlation between both "Sales" and "Discount" and "Profit" and "Discount"
# No correlation between quantity and profit.Cost should be reduced in some areas to increase the profit.
# Give extra effort in segment area.
# Increase the shipping mode.
# Many states needs improvement in terms of category and sub-category,they should be sell at reasonable price.
# The Standard class shipment mode is most preferred by the customers where as the Same Day shipment mode is least preferred.
# We see the sales are very high for the states California, New York and Texas. However the sales are very low for states like Maine, West Virginia, North datoka
# **
