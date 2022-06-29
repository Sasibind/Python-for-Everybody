hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
pay = h*r
h = h - 40
if h>0:
    pay = pay + 0.5*h*r
print(pay)