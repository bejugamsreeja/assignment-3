#!/usr/bin/env python
# coding: utf-8

# In[1]:


## write a python function to sum all the numbers in a list

num = (8, 2, 3,0,7)
total = 0
for x in num:
    total += x 

print(total)


# In[2]:


## write a python function to sum all the numbers in a list

def total(l):
    s=0
    for i in l:
        s=s+i
    return s
n=list(map(int,input().split(',')))
print(total(n))


# In[3]:


## write a python program to reverse a string

def my_function(x):
    return x[::-1]

mytxt = my_function("1234abcd")

print(mytxt)


# In[4]:


## write a python function that accepts a string and calculate the number of upper case letters and lower case letters

def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brow Fox')


