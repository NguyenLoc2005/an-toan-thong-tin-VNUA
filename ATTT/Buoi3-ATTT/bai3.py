#Bài 3
#Tìm nghịch đảo
#Mã hóa và giải mã El-Gamal
#Tạo khóa
def tim_nghich_dao(a3,b3):
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
  return r2
p = int(input("Nhập p: "))
g = int(input("Nhập g: "))
u = int(input("Nhâp u: "))
k = int(input("Nhập k: "))
y=g**u%p
print("Khóa công khai:(",p+",",g+",",y+")")
print("Khóa mật:",u)
k = int(input("Nhập k: ")) #Nhập k sao cho k/(k,p-1)=1
#Sinh mã
x = int(input("Cho bản rõ X: "))
a=g**k % p
b=y**k * x % p
print("Bản mã là: (",a+",",b+")")
#Giải mã
au_nghich_dao = tim_nghich_dao(p,a**u)
print("Giải mã X: "+str(b*au_nghich_dao%p))