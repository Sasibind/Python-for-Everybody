# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
s = 0
x = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    lpos = line.find(' ')
    s = s + float(line[lpos+1:])
    x = x + 1
    
print("Average spam confidence:", s/x)
