#Viết hàm mã hóa và giải mã Cesar

#Mã hóa Cesar
def ma_hoa_cesar():
    ban_ma = ""
    ban_ro = input("Nhập vào bản rõ: ")
    khoa = int(input("Nhập vào khóa: "))
    
    for ky_tu in ban_ro:
        if 'A' <= ky_tu <= 'Z':    
            vi_tri_moi = (ord(ky_tu) - ord('A') + khoa ) % 26
            ky_tu_ma = chr(vi_tri_moi + ord('A'))
            ban_ma = ban_ma + ky_tu_ma
        elif 'a' <= ky_tu <= 'z':    
            vi_tri_moi = (ord(ky_tu) - ord('a') + khoa) % 26
            ky_tu_ma = chr(vi_tri_moi + ord('a'))
            ban_ma += ky_tu_ma
        else:
            ban_ma += ky_tu       
    return ban_ma

ma_hoa_cesar()

#Giải mã Cesar
def giai_ma_cesar():
    ban_ro = ""
    ban_ma = input("Nhập vào bản mã: ")
    khoa = int(input("Nhập vào khóa: "))

    for ky_tu in ban_ma:
        if 'A' <= ky_tu <= 'Z':    
            vi_tri_moi = ord(ky_tu) - ord('A') - khoa
            # nếu âm → cộng 26
            if vi_tri_moi < 0:
                vi_tri_moi += 26

            ky_tu_ro = chr(vi_tri_moi % 26 + ord('A'))
            ban_ro += ky_tu_ro

        elif 'a' <= ky_tu <= 'z':    
            vi_tri_moi = ord(ky_tu) - ord('a') - khoa
            # nếu âm → cộng 26  
            if vi_tri_moi < 0:
                vi_tri_moi += 26

            ky_tu_ro = chr(vi_tri_moi % 26 + ord('a'))
            ban_ro += ky_tu_ro

        else:
            ban_ro += ky_tu        
    return ban_ro

giai_ma_cesar()
