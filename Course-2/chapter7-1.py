# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
fstr = fh.read().rstrip().upper()
print(fstr)
fh.close()