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
p = int(input("Nhập p: "))
a = int(input("Nhập a: "))
x = int(input("Nhập x: "))
k = int(input("Nhập k: "))
y=a**x%p
print("Kp: ("+str(p)+","+str(a)+","+str(y)+")")
print("Ks: "+str(x))
r=a**k%p
k_nghich_dao = tim_nghich_dao(p-1,k)
X=int(input("Nhập vào X: "))
s=k_nghich_dao*(X-x*r)%10
print("Chữ kí là: "+str(X)+"|"+"("+str(r)+","+str(s)+")")
#Xác minh chữ ký
#y=int(input("Nhập vào y: "))
#r=int(input("Nhập vào r: "))
#p=int(input("Nhập vào p: "))
#s=int(input("Nhập vào s: "))
#a=int(input("Nhập vào a: "))
#if (y**r)*(r**s)%p == a**x %p:
  #print("Chữ ký hợp lệ")