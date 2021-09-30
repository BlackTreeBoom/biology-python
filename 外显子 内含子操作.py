#!/usr/bin/env python
# coding: utf-8

# In[1]:


DNA = "GCTGTGGGGCTCAGTGAGACCATGTCC*TGGCTGGCCAGCTACCTGGAGAATGTGGACCATTTCCCCAGCTCAACCCCTCCCAGGTGACTAGCTCAGGACAAAGCCTCCAGATTCTTCAAAGGAAGATGGGAGGAAGGGAGAAAGC*TGGCTTTCCCACAGCCAAAGCTCCAT*TCTGGCTGAGGCCCCAGGGCCTTGGAGAAGCGAACTGAACTGGCTGATGAACTC*TGAAGTCACTCTCCAGACTCAGTTGCTGGTGGTTTT*CCTTCGTAGCCATCCATAGGTGGCAGAGGAGGGACTTCAGATG*CTTCATGACACCCTCTTTCC"


# In[2]:


DNA.split('*')


# In[4]:


DNA1=DNA.split('*')#分割


# In[6]:


DNAexcon=DNA1[::2]#提取外显子


# In[7]:


len(DNAexcon)#计算外显子数量


# In[12]:


DNA_legh=''.join(DNA1)#拼接整个DNA


# In[14]:


DNA_exlegh=''.join(DNAexcon)#拼接外显子


# In[19]:


a=len(DNA_legh)#分别计算对应长度，最后计算占比
print(a)
b=len(DNA_exlegh)
print(b)
a=float(a)
b=float(b)
print('percent: {:.2%}'.format(b/a))


# In[20]:


DNAintron=DNA1[1::2]#提取内含子


# In[22]:


INTRON=[x.lower() for x in DNAintron]
EXCON=[x.upper() for x in DNAexcon]


# In[23]:


print(INTRON)
print(EXCON)


# In[24]:


#insert(),在l第2个元素前插入一个元素'X'
EXCON.insert(1,'tggctggccagctacctggagaatgtggaccatttccccagctcaacccctcccaggtgactagctcaggacaaagcctccagattcttcaaaggaagatgggaggaagggagaaagc')


# In[25]:


print(EXCON)


# In[26]:


EXCON.insert(3,'tctggctgaggccccagggccttggagaagcgaactgaactggctgatgaactc')
EXCON.insert(5,'ccttcgtagccatccataggtggcagaggagggacttcagatg')


# In[27]:


print(EXCON)


# In[28]:


DNA_EX_IN=''.join(EXCON)


# In[29]:


print(DNA_EX_IN)#外显子全部为大写，内含子全部为小写


# In[30]:


DNA_MIX=''.join(DNA1)#拼接DNA完整序列
print(DNA_MIX)


# In[45]:


def DNA_complement(sequence):#定义互补RNA序列
    sequence = sequence.upper()
    sequence = sequence.replace('A', 'u')
    sequence = sequence.replace('T', 'a')
    sequence = sequence.replace('C', 'g')
    sequence = sequence.replace('G', 'c')
    return sequence.upper()


# In[46]:


DNA_complement(DNA_MIX)


# In[ ]:




