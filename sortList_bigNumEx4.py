lst = []
n_elements = int(input(" Enter number of elements :"))
for i in range(0, n_elements):
    ele = int(input())
  
    lst.append(ele) # adding the element
      
print(lst)
lst.sort(reverse = True)
print(lst)
n = int(input("Enter the smallest numbers in list to remove :"))
del lst[n_elements - n : ]
print(lst)