#Giải bài toán xếp ba lô
n=int(input("Nhập vào số lượng của giá trị của vecto siêu tăng: "))
vec_to = []
dem=0
kq = []
for i in range(n):
    z = int(input("Giá trị " + str(i+1)+ "của vecto siêu tăng: "))
    dem = dem +1
    vec_to.append(z)


t=int(input("Nhập T: "))

for i in range(dem):
    if t>max(vec_to) or t==max(vec_to): 
        xj=1
    else:
        xj=0
    
    kq.append(xj)
    t= t - max(vec_to)*xj

    vec_to.remove(max(vec_to))
for x in reversed(kq):
    print(x)

