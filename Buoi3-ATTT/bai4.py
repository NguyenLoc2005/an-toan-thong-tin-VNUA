#Chữ ký & RSA

def tim_nghich_dao(a3,b3):
  moudle = a3
  a1=1
  a2=0
  b1=0
  b2=1
  q=a3//b3
  r3=a3-b3*q
  r2=a2-b2*q
  while r3!=1:
    a3=b3
    b3=r3
    a2=b2
    b2=r2
    q=a3//b3
    r3=a3-b3*q
    r2=a2-b2*q
  if r2<0:
    r2 = r2 + moudle
  return r2

def chu_ky_rsa():
  p=int(input("Nhập vào p: "))
  q=int(input("Nhập vào q: "))
  e=int(input("Nhập vào e: "))
  n=p*q
  m=(p-1)*(q-1)
  d=tim_nghich_dao(m,e)

  print("Khóa công khai: (", e, ",", n, ")")
  print("Khóa bí mật: (", d, ",", p, ",", q, ")")

  #Tạo chữ ký điện tử
  x = int(input("Cho bản rõ X: "))
  print("sig(x)=",(x**d)%n)
  print("Thông điệp gửi đi "+str(x)+"||"+str((x**d)%n))
  print("Xác minh chữ ký")
  y = int(input("Cho Y: "))
  if (y**e)%n == x:
    print("Đúng chữ ký")
  else:
    print("Sai chữ ký")

chu_ky_rsa()

