#Chữ kí El-Gamal

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
      r2=r2+moudle
  return r2

def chu_ky_el_gamal():
  p = int(input("Nhập p: "))
  a = int(input("Nhập a: "))
  x = int(input("Nhập x: "))
  k = int(input("Nhập k: "))
  y=a**x%p
  print("Kp: ("+str(p)+","+str(a)+","+str(y)+")")
  print("Ks: "+str(x))
  
  k_nghich_dao = tim_nghich_dao(p-1,k)
  X=int(input("Nhập vào X: "))
  r=a**k%p
  s=k_nghich_dao*(X-x*r)%(p-1)
  print("Chữ kí sig ("+str(X)+","+str(k)+") = ("+str(r)+","+str(s)+")")
  print("Văn bản gửi đi X||(r,s) = "+str(X)+"||("+str(r)+","+str(s)+")")

  #Xác minh
  X1=int(input("Nhập vào X: "))
  r1=int(input("Nhập vào r: "))
  s1=int(input("Nhập vào s: "))
  if (a**x)%p == (y**r1)*(r1**s1):
    print("Chữ ký hợp lệ")

chu_ky_el_gamal()