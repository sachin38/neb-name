#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

def main():
    print "Enter the first symbol number: ",
    start_num = int(raw_input())
    print "Enter the last symbol number: ",
    end_num = int(raw_input())
    symbol_list = range(start_num, end_num + 1)

    for symbol_number in symbol_list:
        namefetch(symbol_number)

def namefetch(symbolnumber):
    data = {
      "keyword": symbolnumber,
      "slug": "SearchResult"
    }
    req = requests.post("http://www.neb.gov.np/result/search", data=data)
    response = req.text
    soup = BeautifulSoup(response, "html.parser")

    h1_text = soup.find("h1", {"class": ["text-success text-center", "text-danger text-center"]}).text
    if "Congratulation" in h1_text:
        name = h1_text.lstrip("Congratulations!! ").rstrip(", ")
    else:
        name = h1_text.lstrip("Sorry!! ").rstrip(", ")
    
    print name,symbolnumber
    text_file = open('students.txt', 'a')
    text_file.write(str(name))
    text_file.write(" ")
    text_file.write(str(symbolnumber))
    text_file.write("\n")
    text_file.close()

main()
