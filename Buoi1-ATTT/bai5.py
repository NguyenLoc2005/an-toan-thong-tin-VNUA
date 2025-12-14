#Viết chương trình nhập vào giá trị tháng, năm, cho biết tháng đó có bao nhiêu ngày

thang = int(input("Nhập vào tháng: "))
nam = int(input("Nhập vào nam: "))

if thang==1 or thang==3 or thang==7 or thang==8 or thang==10 or thang==12:
    print("Có 31 ngày")
elif thang==4 or thang==6 or thang==9 or thang==11:
    print("Có 30 ngày")
elif thang==2 and nam%4==0 and nam%100!=0:
    print("29 ngày")
elif thang==2:
    print("28 ngày")
else:
    print("Nhập tháng từ 1-12 nhé")