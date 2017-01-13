#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

print "Enter the symbol number of student: ",
symbol = raw_input()

url = "http://www.neb.gov.np/results/search?SYMB="+str(symbol)+"&btn=Search"
req = requests.get(url)
response = req.text
soup = BeautifulSoup(response, "lxml")
td = soup.find("td", {"class" : "borderResult"})
div = td.find("div")
p = div.find("p")
to_be_split = p.text
data = to_be_split.split(",")
name = data[0].replace(".","")
name = name[19:]
print "NAME: ",
print name
