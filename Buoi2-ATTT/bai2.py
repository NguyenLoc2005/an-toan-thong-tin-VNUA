#Viết hàm tìm nghịch đảo theo modun đồng dư

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

print(tim_nghich_dao_theo_mo_dun_dong_du(17,33))