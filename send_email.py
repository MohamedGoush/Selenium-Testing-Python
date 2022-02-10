import imp
from urllib import response
from h11 import Data
import requests # HTTP Request

from bs4 import BeautifulSoup # Web Scrapping

import smtplib   # Send The Mail

import datetime # Get Current Data and Time

now = datetime.datetime.now()

# print(datetime.datetime.now())

content = ''

# Extracting Hacker News Stories.

def extract_news(url):
    print("Extracting Hacker News Stories...")
    cnt = ''
    cnt += ('<b>HackerNews Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        cnt += ((str(i+1)+' :: '+tag.text+"\n"+'<br>')if tag.text!='More' else '')


