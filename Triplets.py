n = int (input("Enter a number :"))
for i in range (0,n):
    for j in range (0,n):

        for k in range (0,n):
            print(chr(97+i)+chr(97+j)+chr(97+k))
            