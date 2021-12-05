#!/usr/bin/env python
# coding: utf-8

# In[26]:


import requests
from bs4 import BeautifulSoup
import re


# In[39]:


URL = "https://twitter.com/home/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

t_soup = [s.get_text() for s in soup.find_all(lambda tag: tag.name == 'div' and 
                                   tag.get('class') == ['product'])]

tweets = '\n'.join(t_soup)
print(tweets)


# In[28]:


searched_word = input('cellphone / email ')


# In[32]:


results = soup.body.find_all(string=re.compile('.*{0}.*'.format(searched_word)), recursive=True)

print( 'Found the word "{0}" {1} times\n'.format(searched_word, len(results)))


# In[33]:


print(results.prettify())

