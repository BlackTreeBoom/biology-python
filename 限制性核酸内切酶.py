#!/usr/bin/env python
# coding: utf-8

# In[1]:


DNA='gaattcctcgagctagcGGATCCcaccatggtgagcaagggcgACGCGTaggagctgttcaccggggtggtgcccatcctggtcgagctggacggcgacgtaaacggccacaagttcagcgtgtccggcgagggcgagggcgatgccacctacggcaagctgaccctgagaattcagttcatctgcaccaccggcaagGATATCctgcccgtgccctggGGATCCcccaccctcgtgaccaccctgacctacggcgtgcagtgcttcaGGATCCgccgctaccccgaccacatgaagcagcacgacttcttcaagtccgccatgcccg'


# In[2]:


Enzyme={'EcoRI':'G/AATTC','BamHI':'G/GATCC','EcoRV':'GAT/ATC','Mlul':'A/CGCGT'}#生产限制酶字典


# In[3]:


print(Enzyme)


# In[4]:


DNA_new=DNA.upper()
print(DNA_new)


# In[10]:


EcoRI_1 =DNA_new.count("GAATTC")#计算EcoRI酶切位点数
EcoRI_2 =DNA_new.count("CTTAAG")
print(EcoRI_1 + EcoRI_2)
BamHI_1 =DNA_new.count("GGATCC")#计算BamHI酶切位数
BamHI_2 =DNA_new.count("CCTAGG")
print(BamHI_1+BamHI_2)
EcoRV_1 =DNA_new.count("GATATC")#计算EcoRV酶切位数
EcoRV_2 =DNA_new.count("CTATAG")
print(EcoRV_1+EcoRV_2)
Mlul_1 =DNA_new.count("ACGCGT")#计算Mlul酶切位数
Mlul_2 =DNA_new.count("TGCGCA")
print(Mlul_1+Mlul_2)


# In[12]:


EcoRV_cut_place=DNA_new.find('GATATC')#计算EcoRV切割位点
print(EcoRV_cut_place)


# In[13]:


EcoRV_cut=DNA_new[:198]#截取EcoRV酶切位点上流片段
print(EcoRV_cut)


# In[14]:


Mlul_cut_place=DNA_new.find('ACGCGT')#计算Mlul切割位点
print(Mlul_cut_place)


# In[15]:


Mlul_cut=DNA_new[:43]#截取EcoRV酶切位点上流片段
print(Mlul_cut)


# In[ ]:




