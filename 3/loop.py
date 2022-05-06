from re import X


list = [1,2,3,4,5]

for element in list:
    if element == 4:
        continue
    print(element)

x = 1
while x < 5:
   if x == 3:
       x = x + 1
       continue
    print(x)
    x = x + 1
