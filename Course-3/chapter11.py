import re

filename = input("Enter file name: ")
if len(filename) < 1: filename = "regex-sum-1583849.txt"

fh = open(filename)

text = fh.read()

nums = re.findall('[0-9]+', text)
sum = 0

for num in nums:
    num = int(num)
    sum += num

print(sum)

fh.close()