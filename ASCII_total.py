from math import sqrt
n = int (input("Enter a range:"))
sum=0
for i in range (n):
   username = input('Enter Your Characters :\n')
   sum += ord(username)
   
print(sum)   

