#Nhập vào chiều dài 3 cạnh của tam giác, kiếm tra tính hợp lệ của 3 giá trị nhập vào, nếu hợp lệ, tính diện tích và chu vi của tam giác
a = float(input("Nhập vào cạnh thứ nhất: "))
b = float(input("Nhập vào cạnh thứ hai: "))
c = float(input("Nhập vào cạnh thứ ba: "))

if a+b<=c or b+c<=a or c+a<=b:
    print("3 cạnh không tạo nên 1 tam giác")
else:
    print("Chu vi của tam giác là: ",a+b+c)
    print("Diện tích của tam giác là: ",a*b*c)