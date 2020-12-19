'''
In this assignment you will write a Python program, The program will prompt for a URL,
read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data,
compute the sum of the numbers in the file and enter the sum below:
sample file where we give you the sum for your testing and the other is the actual data you need to process
Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1004021.json (Sum ends with 10)
'''
import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Website URL: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print("Retrieved",len(data))
info = json.loads(data)
sum = 0
count = 0
for item in info['comments']:
    item = item['count']
    sum = sum + int(item)
    count += 1
print("count:",count)
print("sum:", sum)
