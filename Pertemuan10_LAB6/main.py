from data import codelab6

print("PROGRAM MENAMPILKAN DAFATR NILAI MAHASISWA")
while True:
    print("")
    c =input("(L)lihat, (T)ambah, (U)bah, (H)apus, (K)eluar : ")
    if c.lower() == 't':
        codelab6.tambah()

    elif c.lower() == 'u':
        codelab6.ubah()

    elif c.lower() == 'l':
        codelab6.lihat()

    elif c.lower() == 'h':
        codelab6.hapus()

    elif c.lower() == 'k':
        print("Keluar")
        break
