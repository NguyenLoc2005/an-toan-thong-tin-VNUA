#Số nguyên tố

x = int(input("Nhập vào x: "))

if x < 2:
    print(x, "không là số nguyên tố")
else:
    la_so_nguyen_to = True
    for i in range(2, x):
        if x % i == 0:
            la_so_nguyen_to = False
            break

    if la_so_nguyen_to:
        print(x, "là số nguyên tố")
    else:
        print(x, "không là số nguyên tố")
