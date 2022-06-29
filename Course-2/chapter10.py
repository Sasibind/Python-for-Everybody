name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
dic = dict()

for line in handle:
    if line.startswith("From "):
        arr = line.split()
        s = arr[-2]
        s1 = s.split(':')
        #print(s1)
        t = s1[0]
        #print(t)
        
        dic[t] = dic.get(t, 0) + 1
        #print(dic[t], t)
    
ls = list()
for key, val in dic.items():
    tp = (key,val)
    ls.append(tp)

ls = sorted(ls)

for key,val in ls: print(key,val)