A = input("Masukkan deret angka : ")
B = 0
C = (A.split(","))
print("Total :",end=" ")
for D in C:
    D=int(D)
    if D%2==1:
        B = B-D
        print(D*-1, end=" ")
    else:
        B = B+D
        print("+",D,end=" ")
print()
print("Hasil perhitungan diatas ialah", B)