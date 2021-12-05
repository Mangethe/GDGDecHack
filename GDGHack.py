#!/usr/bin/env python
# coding: utf-8

# In[26]:

def getdetailsmudge:
  
  import requests
  from bs4 import BeautifulSoup
  import re




  URL = "https://twitter.com/"
  page = requests.get(URL)

  soup = BeautifulSoup(page.content, "html.parser")


  searched_input = input('cellphone / email / Twitter handle')



  results = soup.body.find_all(string=re.compile('.*{0}.*'.format(searched_input)), recursive=True)

  print( 'Found the word "{0}" {1} times\n'.format(searched_input, len(results)))
  
  if len(results) > 0:
    answer = input('Do you want to keep your data visible?  Y/N')
    if answer == 'N':
      for item in searched_input:
        searched_input = item[:1] + '*********'
    else:
      print('It is not safe to keep your personal data visible)
      


  



