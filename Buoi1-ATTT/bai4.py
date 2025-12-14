#Nhập vào chiều dài 3 cạnh của tam giác, kiếm tra tính hợp lệ của 3 giá trị nhập vào, nếu hợp lệ, tính diện tích và chu vi của tam giác

import math

a = float(input("Nhập vào cạnh thứ nhất: "))
b = float(input("Nhập vào cạnh thứ hai: "))
c = float(input("Nhập vào cạnh thứ ba: "))

if a+b<=c or b+c<=a or c+a<=b:
    print("3 cạnh không tạo nên 1 tam giác")
else:
    p=(a+b+c)/2
    print("Chu vi của tam giác là: ",p)
    print("Diện tích của tam giác là: ",math.sqrt(p*(p-a)*(p-b)*(p-c)))