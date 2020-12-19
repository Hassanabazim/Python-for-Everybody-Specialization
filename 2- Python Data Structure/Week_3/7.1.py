'''
7.1 Write a program that prompts for a file name, then opens that file and reads through the file,
and print the contents of the file in upper case. Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt
'''
file = input("Enter file name: ")
try:
    fh = open(file)
except:
    print("there no file in that name in our Database")
    quit()
fh = open(file)
txt = fh.read()
txt_upper = txt.upper()
txt_space = txt_upper.strip()
print(txt_space)
