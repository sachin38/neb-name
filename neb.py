#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

print "Enter first symbol number: ",
first_symbol = int(raw_input())

print "Enter the last symbol number: ",
last_symbol = int(raw_input())

symbol_list = range(first_symbol, last_symbol+1)


for symbol in symbol_list:
    url = "http://www.neb.gov.np/results/search?SYMB="+str(symbol)+"&btn=Search"
    try:
        req = requests.get(url)
        
    except requests.exceptions.RequestException as e:
        print e
        sys.exit(1)
    
    response = req.text
    soup = BeautifulSoup(response, "lxml")
    td = soup.find('td', {'class' : 'borderResult'})
    div = td.find('div')
    p = div.find('p')
    to_be_split = p.text
    data = to_be_split.split(',')
    name = data[0].replace(".","")
    dob =  data[1].replace(".","")
    name = name[19:]
    dob = dob[13:]
    
    print "*********\n"
    print "SYMBOL: ",symbol
    print "NAME: ",name
    print "DATE OF BIRTH: ",dob
    result = soup.findAll("div")
    status = result[43].text
    print "MARKS AND RESULT: ",status
    print "*********\n"
    
    text_file = open("students.text", "a")
    text_file.write("NAME: ")
    text_file.write(str(name.encode("utf-8")))
    text_file.write("\n")
    text_file.write("Symbol no: ")
    text_file.write(str(symbol))
    text_file.write("\n")
    text_file.write("DATE OF BIRTH: ")
    text_file.write(str(dob))
    text_file.write("\n")
    text_file.write("RESULT STATUS: ")
    text_file.write(str(status))
    text_file.write("\n**************************\n\n")
    text_file.close()
