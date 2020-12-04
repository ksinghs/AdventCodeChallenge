#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Challanege 1
list = open('C:\\Users\\hp\\Strive_AI_AdventCode\\Challenge1\\input.txt').read().splitlines()
sum = 2020
for i in range(len(list)):
    for j in range(i+1, len(list)):
        a = int(list[i])
        b = int(list[j])
        if a+b == sum : print(a,b,a*b)


# In[2]:


#challenge 2
list = open('C:\\Users\\hp\\Strive_AI_AdventCode\\Challenge1\\input.txt').read().splitlines()
sum = 2020
for i in range(len(list)):
    for j in range(i+1, len(list)):
        for k in range(i+2, len(list)):
            a = int(list[i])
            b = int(list[j])
            c = int(list[k])
            if a+b+c == sum : print(a,b,c,a*b*c)


# In[ ]:




