#Tìm ước chung lớn nhất

def ucln(a ,b):
    while b!=0:
        r=a%b
        a=b
        b=r
    return a
print(ucln(6,8))