#Nhập vào 1 xâu họ tên người Việt. Tách ra từ chỉ họ đệm, tên

ho_ten = input("Nhập vào họ tên người Việt: ")
xem_phan_tu = ho_ten.split()
dem_phan_tu = len(xem_phan_tu)
ho = xem_phan_tu[0]
ten_dem = xem_phan_tu[1:dem_phan_tu-1]
ten = xem_phan_tu[dem_phan_tu-1]
print("Họ là: ",ho)
print("Tên đệm là: ",ten_dem)
print("Tên là: ",ten)
