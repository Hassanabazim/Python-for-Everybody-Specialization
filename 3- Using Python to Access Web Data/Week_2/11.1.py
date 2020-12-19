'''
In this assignment you will read through and parse a file with text and numbers.
You will extract all the numbers in the file and compute the sum of the numbers.
We provide two files for this assignment. One is a sample file where we give you the sum for your testing
and the other is the actual data you need to process for the assignment.
Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
Actual data: http://py4e-data.dr-chuck.net/regex_sum_1004016.txt (There are 84 values and the sum ends with 310)
'''
import re
file = input("Enter the file name:")
try:
    fh = open(file)

except:
    print("The file does not exist!")
    quit()

ft = fh.read()
sum = 0
line = re.findall("[0-9]+",ft)
for str in line:
    num = int(str)
    sum = sum + num
print("sum =", sum)
