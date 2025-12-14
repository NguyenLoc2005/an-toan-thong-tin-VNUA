#Đề bài: Viết chương trình tìm giá trị lớn nhất trong 3 số

import math

a = float(input("Nhập vào số a: "))
b = float(input("Nhập vào số b: "))
c = float(input("Nhập vào số c: "))
#Cách 1
print("Giá trị lớn nhất là:",  max(a,b,c))
#Cách 2
if a>b and a>c:
    print("Giá trị lớn nhất là:",  a)
elif b>a and b>c:
    print("Giá trị lớn nhất là:",  b)
else:
    print("Giá trị lớn nhất là:",  c)