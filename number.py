#!/usr/bin/env python
# coding: utf-8

# A module called number which implements two functions: check_even_odd
# andcheck_positive_negative.
# 

# In[12]:


def even(x):
    return((x % 2) == 0)
def odd(x):
    return((x % 2) != 0)
def positive(x):
    return(x>0)
def negative(x):
    return(x<0)

