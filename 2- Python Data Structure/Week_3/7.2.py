'''
7.2 Write a program that prompts for a file name, then opens that file
and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines
and compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt.
'''
file = input("Enter the file name: ")
try:
    fh = open(file)
except:
    print("File does not exist!")
    quit()

count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    pos = line.find(":")
    num = line[pos+2:]
    number = float(num)
    count = count + 1
    total = total + number

avg = total / count
print("Average spam confidence:",avg)
