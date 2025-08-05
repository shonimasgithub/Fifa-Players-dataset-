#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[3]:


fifa=pd.read_csv("C:\\Users\\SHONIMA S\\Downloads\\fifa_data.csv")
print(fifa)


# In[4]:


#1.Which country has the most number of players (score :1)
"""insight:England has the most no. of players with 1662 players"""
nat=fifa["Nationality"].value_counts()
nat1=nat.head()
print(nat1)


# In[5]:


#2.Plot a bar chart of 5 top countries with the most number of players.
"""insight:As we can see from the graph England has the most no.of players with 1600 above players,in the second position we can see Germany with almost 1200 players,after England comes Spain with just above 1000 players,in the 4th position comes Argentina with 900 above players and in 5th position with nearly same players as in Argentina"""
x=["England","Germany","Spain","Argentina","France"]
y=[1662,1198,1072,937,914]
plt.bar(x,y,width=0.5,color="black")
plt.show()


# In[7]:


#3.Which player has the highest salary?
"""insight:Argentine player Lionel Messsi has the highest salary with 565000.0$"""
fifa[fifa.columns[12]]=fifa[fifa.columns[12]].replace('[^.0-9]','',regex=True).astype(float)
fifa['Wage']


# In[8]:


fifa[['Name','Nationality','Wage']][fifa['Wage']==fifa['Wage'].max()]


# In[9]:


#4.Plot a histogram to get the salary range of the players.
"""insight:A majority of the players are having a salary around 50k"""
plt.hist('Wage',data=fifa)
plt.title("Salary range of players")
plt.xlabel("salary")
plt.ylabel("number of players")
plt.show()


# In[11]:


fifa[fifa.columns[12]]=fifa[fifa.columns[12]].replace('[^.0-9]','',regex=True).astype(float)

fifa['Wage']


# In[12]:


#5.Who is the tallest player in the fifa? 
"""insight:There are two players with the height 6'9,one is T.Holy from Czech Republic and the other player is D. Hodzic from Croatia.They are the tallest of all other players in fifa."""
ht=fifa.sort_values(by="Height",ascending=False)
ht[["Name","Height","Nationality"]].head()


# In[13]:


#6.Which club has the most number of players?
"""insight:26 clubs have the most no.of players with each club containing 33 players."""
club=fifa["Club"].value_counts()
club1=club.head(26)
print(club1)


# In[14]:


#7.Which foot is most preferred by the players?Draw a bar chart for preferred foot
""""""
foot=fifa["Preferred Foot"].value_counts()
print(foot)
foot.plot(kind="bar",color="k")
plt.title("PREFFERED FOOT BY PLAYERS",color="r")
plt.xlabel("preffered foot")
plt.ylabel("no.of players")
plt.show()


# In[15]:


fifa.info()


# In[16]:


fifa["Nationality"].value_counts()


# In[17]:


fifa.duplicated().sum()


# In[18]:


print(fifa.isnull())
print(fifa.isnull().sum())


# In[ ]:




