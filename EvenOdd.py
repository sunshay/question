#!/usr/bin/python

a = [1,2,3,4,5,6,7,8,9,10,23,45,6]
for i in a:
    if i % 2 == 0:
        print(str(i) + "is Even")
    else:
        print(str(i) + "is Odd")