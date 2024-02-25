#!/usr/bin/env python
# coding: utf-8

# In[1]:


elements = ['*', 'hello', -87.8, '-', '/', '+', 6]

for element in elements:
    if isinstance(element, (int, float)):
        print(f'{element} is a value.')
    elif isinstance(element, str):
        print(f'\'{element}\' is a value.')
    else:
        print(f'{element} is an expression.')

