'''
In this assignment you will write a Python program,The program will prompt for a URL,
read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data,
compute the sum of the numbers in the file.We provide two files for this assignment.
sample file where we give you the sum for your testing and the actual data you need to process for the assignment.
Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1004020.xml (Sum ends with 87)
'''
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Website URL: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved:', len(data), 'characters')
data.decode()
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
print("Count:",len(lst))
sum = 0
for num in lst :
    num = num.find('count').text
    sum = sum + int(num)
print("Sum:",sum)
