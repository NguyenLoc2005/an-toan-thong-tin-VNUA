#Viết hàm mã hóa và giải mã Vigenere

print("Mã hóa vigenere")
def ma_hoa_vigenere():
    ban_ro = input("Nhập vào bản rõ: ")
    khoa = input("Nhập vào khóa: ")
    so_ky_tu_khoa = len(khoa)
    index=0
    ban_ma = ""

    for ky_tu in ban_ro:
        if 'A' <= ky_tu <= 'Z':
            p=ord(ky_tu)-ord('A')
            k=ord(khoa[index%so_ky_tu_khoa])-ord('A')
            c=(p+k)%26
            ban_ma = ban_ma + chr(c+ord('A'))
            index = index + 1
            
        elif 'a' <= ky_tu <= 'z':
            p=ord(ky_tu)-ord('a')
            k=ord(khoa[index%so_ky_tu_khoa])-ord('a')
            c=(p+k)%26
            ban_ma = ban_ma + chr(c+ord('a'))
            index = index + 1

        else:
            ban_ma += ky_tu

    return ban_ma
print(ma_hoa_vigenere())

print("Giải mã vigenere")
def giai_ma_vigenere():
    ban_ma = input("Nhập vào bản mã: ")
    khoa = input("Nhập vào khóa: ")
    so_ky_tu_khoa = len(khoa)
    index=0
    ban_ro=""

    for ky_tu in ban_ma:
        if 'A' <= ky_tu <= 'Z':
            c=ord(ky_tu)-ord('A')
            k=ord(khoa[index%so_ky_tu_khoa])-ord('A')
            p=(c-k)%26
            ban_ro = ban_ro + chr(p+ord('A'))
            index = index + 1
        elif 'a' <= ky_tu <= 'z':
            c=ord(ky_tu)-ord('a')
            k=ord(khoa[index%so_ky_tu_khoa])-ord('a')
            p=(c-k)%26
            ban_ro = ban_ro + chr(p+ord('a'))
            index = index + 1

        else:
            ban_ro += ky_tu

    return ban_ro
