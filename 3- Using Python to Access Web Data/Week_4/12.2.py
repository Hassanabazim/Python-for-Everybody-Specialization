'''
Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program
The program will use urllib to read the HTML from the data files below, and parse the data,
extracting numbers and compute the sum of the numbers in the file, We provide two files for this assignment.
One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1004018.html (Sum ends with 62)
To run this, download the BeautifulSoup zip file
http://www.py4e.com/code3/bs4.zip
and unzip it in the same directory as this file
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#use BeautifulSoup libaray to get all context in html page
url = input('Enter The Website URL: ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
#minimize the html page data bet <span>
tags = soup('span')
#extract the numbers thats in html page
sum = 0
count = 0
for tag in tags:
    sum = sum + int(tag.contents[0])
    count += 1
print("Count:",count)
print("sum:",sum)
