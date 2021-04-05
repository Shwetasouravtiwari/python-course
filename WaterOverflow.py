n = int (input("Enter a number of line:"))
capacity = 255
sum =0
for i in range(0,n):
    i + 1
    liter = int (input("Enter liter:\n"))
    if (sum + liter > capacity):
        print("Insufficient capacity!")
    else:
        sum = sum + liter

print("Total liters : ", sum)    
