
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("Expanded_data_with_more_features.csv")
print(df.head())


# In[3]:


df.describe()


# In[4]:


df.info()


# In[5]:


df.isnull().sum()


# # Drop unnamed column

# In[6]:


df=df.drop("Unnamed: 0",axis=1)
print(df.head)


# In[7]:


plt.figure(figsize = (4,4))
ax = sns.countplot(data = df,x = "Gender")
ax.bar_label(ax.containers[0])
plt.show()


# In[9]:


plt.figure(figsize=(5, 5))
ax = sns.countplot(data=df, x="Gender")

# Add bar labels manually
for p in ax.patches:    
    height = p.get_height()
    ax.annotate(f'{int(height)}', 
                (p.get_x() + p.get_width() / 2., height),
                ha='center', va='bottom', 
                fontsize=10, color='black', xytext=(0, 5),
                textcoords='offset points')

plt.tight_layout()
plt.show()


# In[11]:


gb = df.groupby("ParentEduc").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
print(gb)


# In[16]:


sns.heatmap(gb,annot = True)
plt.title("Relationship between Parent's Education and Student'S score")
plt.show()


# In[14]:


gb1 = df.groupby("ParentMaritalStatus").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
print(gb1)


# In[18]:


sns.heatmap(gb1,annot = True)
plt.title("Relationship between Parent's Marital status and Student's score")
plt.show()


# In[27]:


sns.boxplot(data = df,x = "MathScore")
plt.show()


# In[25]:


sns.boxplot(data = df,x = "ReadingScore")
plt.show()


# In[26]:


sns.boxplot(data = df,x = "WritingScore")
plt.show()


# In[28]:


print(df["EthnicGroup"].unique())


# In[29]:


groupA = df.loc[(df['EthnicGroup'] == "group A")].count()
print(groupA)


# In[52]:


groupA = df.loc[(df['EthnicGroup'] == "group A")].count()

groupB = df.loc[(df['EthnicGroup'] == "group B")].count()

groupC = df.loc[(df['EthnicGroup'] == "group C")].count()

groupD = df.loc[(df['EthnicGroup'] == "group D")].count()

groupE = df.loc[(df['EthnicGroup'] == "group E")].count()

l = ["group A", "group B", "group C", "group D", "group E"]
mlist = [
    groupA["EthnicGroup"],
    groupB["EthnicGroup"],
    groupC["EthnicGroup"],
    groupD["EthnicGroup"],
    groupE["EthnicGroup"]
]
plt.pie(mlist, labels=l, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.show()


# In[54]:


ax = sns.countplot(data = df, x = 'EthnicGroup')
ax.bar_label(ax.containers[0])

