'''
10.2 Write a program to read through the mbox-short.txt
and figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time
and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''
file = input("Enter the file:")
try:
    fh = open(file)
except:
    print("The file does not exist")
    quit()

database = dict()
for line in fh:
    if not line.startswith("From "): continue
    words = line.split()
    time = words[5].split(':')
    hour = time[0]
    database[hour] = database.get(hour,0) + 1

lst = list()
for key, val in database.items():
    list = (key,val)
    lst.append(list)
lst = sorted(lst, reverse = False)

for val, key in lst:
    print(val,key)
