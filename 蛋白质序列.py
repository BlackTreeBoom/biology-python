#!/usr/bin/env python
# coding: utf-8

# In[1]:


PepA='MDDDIAALVVDNGSGMCKAGF'
PepB='ILTLKYPIEHGIVTNWDDME'


# In[2]:


def frequency(text):#查询字符串种类与频率
    text = text.lower()
    dict = {}
    for char in text:
        keys = dict.keys()
        if char in keys:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict


# In[3]:


PepA = frequency(PepA)


# In[4]:


PepA


# In[6]:


PepB 


# In[16]:


def qPCRlen(DNA):
  qPCRlen_1=len(DNA)
  qPCRlen_2=DNA.count('A')+DNA.count('T')+DNA.count('C')+DNA.conut('G')
  if qPCRlen_1==qPCRlen_2 :
    print("长度相同，无其他序列,可以使用")
  else :
    print("长度不同，有其他序列,不可使用")


# In[17]:


qPCRlen(PepA)


# In[ ]:




