#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

print "Enter your Symbol number: ",
number = raw_input()

data = {
  'keyword': number,
  'slug': 'SearchResult'
}

req = requests.post('http://www.neb.gov.np/result/search', data=data)
response = req.text
soup = BeautifulSoup(response, 'html.parser')

# Gives output like: Congratulation!! FirstName LastName ,
h1_text = soup.find('h1', {'class': ['text-success text-center', 'text-danger text-center'] }).text

# Extract only name from that text
if "Congratulation" in h1_text:
    name = h1_text.lstrip('Congratulation!! ').rstrip(', ')
else:
    name = h1_text.lstrip('Sorry!! ').rstrip(', ')

print name
