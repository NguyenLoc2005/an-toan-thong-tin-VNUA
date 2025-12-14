#Bai 1

x = int(input("Nhập vào x: "))
la_so_nguyen_to = False
for i in range(2,x):
  if x%i==0:
    la_so_nguyen_to = False
    print(x, "không là số nguyên tố")
    break
  else:
    la_so_nguyen_to = True
if la_so_nguyen_to==True:
  print(x, "là số nguyên tố")