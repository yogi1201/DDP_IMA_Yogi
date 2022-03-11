#!/usr/bin/env python
# coding: utf-8

# In[1]:


def case_count(word):
    count={"Uppercase":0, "Lowercase":0}
    for c in word:
        if c.isupper(): #https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/
           count["Uppercase"]+=1
        elif c.islower():
           count["Lowercase"]+=1
        else:
           pass

    print ("('Uppercase :", count["Uppercase"],"'",",","'Lowercase :", count["Lowercase"],"'",")")

case_count("Hello World")


# In[2]:


score = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1, "l": 1, "n": 1, "r": 1, "s": 1, "t": 1,
         "d": 2, "g": 2, "b": 3, "c": 3, "m": 3, "p": 3, "f": 4, "h": 4,"v": 4, "w": 4, "y": 4,
         "k": 5, "j": 8, "x": 8,"q": 10, "z": 10}
         #https://scrabble.hasbro.com/en-us/faq

def get_scrabble_score(word):
    total = 0
    for i in word:
        total = total + score[i.lower()]
    return total


# In[3]:


get_scrabble_score("wibble")


# In[ ]:




