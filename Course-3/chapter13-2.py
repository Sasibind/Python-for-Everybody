import urllib.request
import json

url = input("Enter location: ")

data = urllib.request.urlopen(url).read()

print("Retrieving", url)

info = json.loads(data)

c = 0
s = 0
for item in info['comments']:
    s = s + int(item['count'])
    c += 1

print("Count:", c)
print("Sum:",s)