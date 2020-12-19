'''
9.4 Write a program to read through the mbox-short.txt
and figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address
to a count of the number of times they appear in the file.After the dictionary is produced,
the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''
file = input("Enter the file name: ")
try:
    fh = open(file)
except:
    print("The file does not exist!")
    quit()

inbox = dict()
max_key = None
max_value = None
for line in fh:
    if not line.startswith("From "): continue
    email = line.split()
    index = email[1:2]
    for mail in index:
        inbox[mail] = inbox.get(mail,0) + 1
        for key,value in inbox.items():
            if max_value is None or value > max_value:
                max_value = value
                max_key = key
print(max_key,max_value)
