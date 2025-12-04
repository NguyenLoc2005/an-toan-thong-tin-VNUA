#Viết hàm mã hóa và giải mã Vigenere

def ma_hoa_vigenere():
    ban_ro = input("Nhập vào bản rõ: ")
    khoa = input("Nhập vào khóa: ")
    so_ky_tu_khoa = len(khoa)
    index=0
    ban_ma = ""
    ban_ro = ban_ro.upper()
    khoa = khoa.upper()

    for ky_tu in ban_ro:
        p=ord(ky_tu)-ord('A')
        k=ord(khoa[index%so_ky_tu_khoa])-ord('A')

        c=(p+k)%26
        ban_ma = ban_ma + chr(c+ord('A'))
        index = index + 1
    return ban_ma
#print(ma_hoa_vigenere())

def giai_ma_vigenere():
    ban_ma = input("Nhập vào bản mã: ")
    khoa = input("Nhập vào khóa")
    so_ky_tu_khoa = len(khoa)
    index=0
    ban_ro=""
    ban_ma = ban_ma.upper()
    khoa = khoa.upper()

    for ky_tu in ban_ma:
        c=ord(ky_tu)-ord('A')
        k=ord(khoa[index%so_ky_tu_khoa])-ord('A')

        p=(c-k)%26
        ban_ro = ban_ro + chr(p+ord('A'))
        index = index + 1

    return ban_ro
