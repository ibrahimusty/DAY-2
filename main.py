#Code to find even and odd number
numbers= {1,2,3,4,5,6,7,8,9,10,11,12,14,16,88}
for items in numbers:
    if items % 2 == 0:
       print(f"{items} is an even number")
    else:
        print(f"{items} is an odd number")