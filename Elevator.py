import math
n = int (input("Enter a number of people :"))
p = int (input("Capacitiy :"))
output = n/p
if (n<p):
 print('1')
elif n % p != 0:
 r = math.ceil(output)
 print(r) 
else:
 print(output)
