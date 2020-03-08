#!/usr/bin/env python
# coding: utf-8

# In[78]:


#Practice exercie: week 08
#By Giovani Hernandez Canchola
#Python 3


# In[59]:


#Request a DNA sequence. It must be written in capital letters.


# In[60]:


a = input("Type a DNA sequence: ")


# In[61]:


#Convert the sequence to a list


# In[71]:


b = list(a)


# In[63]:


#Create an empty list, that will store the complementary sequence


# In[72]:


c = []


# In[76]:


#Transform each base pair to their complementary one. Add this information to "c" list.


# In[73]:


for bp in b:
   
    if bp == "A":
        c.extend("T")
    elif bp == "T":
        c.extend("A")
    elif bp == "G":
        c.extend("C")
    elif bp == "C":
        c.extend("G")
    else:
        c.extend("N")


# In[67]:


#Create a new list with elements in reverse order.


# In[74]:


d = c[::-1]


# In[69]:


#Create a new object to convert the reverse list to a string.
#Print it


# In[75]:


e = ''.join(d)
e