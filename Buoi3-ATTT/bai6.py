#Diffe-Hellman

print("Trao chuyển khóa Diffe-Hellman")
def dife_hellman():
    p = int(input("Nhập vào p: "))
    g = int(input("Nhập vào g: "))
    a = int(input("Nhập vào a: "))
    b = int(input("Nhập vào b: "))
    k1=g**a%p
    k2=g**b%p
    print("A->B K1=" +str(k1))
    print("A->B K2=" +str(k2))
    print("Khóa chung")
    A=k2**a%p
    B=k1**b%p
    print("A tính: " +str(A))
    print("B tính: " +str(B))
    
dife_hellman()
