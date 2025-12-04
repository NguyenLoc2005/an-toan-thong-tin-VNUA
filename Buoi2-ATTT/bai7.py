
n = int(input("Nhập vào số lượng của giá trị của vecto siêu tăng: "))
u = int(input("Nhập u: "))
M = int(input("Nhập M: "))
def tim_nghich_dao_theo_mo_dun_dong_du(b3, a3):
    a1=1
    a2=0
    b1=0
    b2=1
    q = a3//b3
    r3 = a3-b3*q
    r2 = a2-b2*q
    while r3!=1:
        a3=b3
        a2=b2
        b3=r3
        b2=r2
        q=a3//b3
        r3 = a3-b3*q
        r2 = a2-b2*q
    return r2
A_phay = []
A = []
for i in range(n):
    z = int(input("Giá trị " + str(i+1)+ "của vecto siêu tăng: "))
    A_phay.append(z)
    a=A_phay[i]*u % M
    A.append(a)

print("Khóa công khai Kp: " + str(A) + "," + str(M))
print("Khóa bí mật Ks: "+ str(u) + ";" + str(tim_nghich_dao_theo_mo_dun_dong_du(u,M)))
