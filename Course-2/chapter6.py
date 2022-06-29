text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(':')
s = text[pos:]
s = s.replace(" ","")
s = float(s)
print(s)