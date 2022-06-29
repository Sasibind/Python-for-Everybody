def computepay(h, r):
    p = h*r
    h = h - 40
    if h>0:
        p = p + 0.5*h*r
    return p

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
p = computepay(h, r)
print("Pay", p)