import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input("Enter location: ")
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
sum = 0

xml = urllib.request.urlopen(url).read()

tree = ET.fromstring(xml)

count_list = tree.findall(".//count")

for value in count_list:
    sum = sum + int(value.text)

print(sum)