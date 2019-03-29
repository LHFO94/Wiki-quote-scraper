#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as soup
import urllib.request


def scrape():
    """This function scrapes that quote of the day from WikiQuotes"""

    #Setting the URL
    my_url = 'https://en.wikiquote.org/wiki/Wikiquote:Quote_of_the_day'
    
    try:
        #Opening up connection with url, get info and close
        request = urllib.request.urlopen(my_url)
        page_html = request.read()
        request.close()
        
        #HTML parsing
        page_soup = soup(page_html,'html.parser')
        
        #Get date and qoute
        date = page_soup.find_all('center')[1]
        qoute = page_soup.find('i')
        author = page_soup.find('td', style='font-size:smaller;')
        
        #Get text from date
        date_txt = date.get_text()
        qoute_txt = qoute.get_text()
        author_txt = author.get_text()
    except Exception as e:
        print(e.message, e.args)
        return 1; 

    #Remove '~\n' & '  ' from str for formatting      
    author_txt = author_txt.replace('~\n', '')
    date_txt = date_txt.replace('~\n', '') 
    qoute_txt = qoute_txt.replace('~\n', '').replace('  ', ' ') 
    
    #Result
    message = date_txt + ' *** ' + qoute_txt + ' *** ' + author_txt
    
    return message






