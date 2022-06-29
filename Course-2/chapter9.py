name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
dic1 = dict()

for line in handle:
    if line.startswith("From "):
        l = line.split()
        dic1[l[1]] = dic1.get(l[1], 0) + 1

maxl = 0
mail1 = ""
for mail in dic1:
    if maxl<dic1[mail]:
        maxl = dic1[mail]
        mail1 = mail

print(mail1, maxl)