A = str(input("Masukkan nama: "))
kursi = []
nama = []
while A != "STOP":
    B = "Masukkan nomor kursi "+A+" : "
    C = input(B)
    if C not in kursi:
        kursi.append(C)
        nama.append(A)
    else:
        print("Mohon maaf kursi tersebut telah terisi!")
    A = str(input("Masukkan nama: "))
print("List kursi yang telah terisi :")
for D in range (len(kursi)):
    print("kursi nomot %s telah diisi oleh %s"%(kursi[D],nama[D]))