#Nhập vào một mảng n số nguyên dương, đếm và in ra các số chia hết cho cả 2 và 5, tính trung bình các số đó

a = []
n = int(input("Nhập vào số lượng số nguyên trong mảng: "))
tong = 0
dem = 0
for i in range(n):
    x = int(input("Phần tử thứ " + str(i+1)+"là: "))
    if x%2==0 and x%5 ==0:
        tong = tong + x
        dem = dem + 1
        a.append(x)
trung_binh = tong/dem
print(a)
print("Có: " +str(dem)+ "số chia hết cho cả 2 và 5")
print("Trung bình cộng các số chia hết cho cả 2 và 5 là: ",trung_binh)