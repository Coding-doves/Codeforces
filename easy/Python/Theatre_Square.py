# needed number of flagstones to cover the surface the Theatre Square.
squ = input()
n, m, a = squ.split(" ")

n = int(n) 
m = int(m) 
a = int(a) 

length = (n // a) + 1 if n % a != 0 else n // a
breath = (m // a) + 1 if m % a != 0 else m // a

flagstones = length * breath
print(flagstones)
