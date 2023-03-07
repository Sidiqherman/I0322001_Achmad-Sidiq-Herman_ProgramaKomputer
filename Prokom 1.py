# program pertama menulis string

print("Assalamualaikum, selamat datang")
print('sekarang kita belajar phyton')
variabel1 = "selamat pagi semuanya"
print(variabel1)
print("====================")


    # # program kedua mengenalkan perbedaan huruf 
Huruf = "Kapital di depan"
huruf = "tidak ada kapital"

print(huruf)
print(Huruf)
print(huruf)


# program UX
# inisiasi variabel
nilai = int(input("masukkan nilai: "))

if nilai >= 85:
    print("==========")
    print("Predikat memuaskan")
    print("==========")
elif nilai >= 75:
    print("==========")
    print("Predikat baik")
    print("==========")
elif nilai >= 60:
    print("==========")
    print("Predikat cukup")
    print("==========")
else:
    print("==========")
    print("anda harus mengulang")
    print("==========")
print("hahahaha")

    # program manipulasi integer

a = int(input("masukkan angka pertama : "))
b = int(input("masukkan angka kedua : "))
print("==========================")
# proses penjumlahan
jumlah = a + b
perkalian = a * b
pengurangan = a - b
pembagian = a / b

print("nilai penjumlahan = ", jumlah)
print("nilai perkalian = ", perkalian)
print("nilai pengurangan = ", pengurangan)
print("nilai pembagian = ", pembagian)

    # program ke lima menghitung
print("===========================")

r = float(input("masukkan jari-jari lingkaran : "))
print("")
pi = 3.1416
keliling = 2 * pi * r
luas = pi * r * r
print("=============================")

print("panjang keliling lingkaran = ", keliling)
print("luas lingkaran = ", luas)
print()
print("========================")

    #program string menggantikan nama pada undangan
tulisan1 = "kepada yth : "
tulisan2 = "nama yang diundang : Agung"
tulisan3 = "alamat kota Surakarta"

print("=========================")
print(tulisan1)
print(tulisan2)
print(tulisan3)
print("=========================")
print(tulisan1)
print(tulisan2.replace("Agung", "Ambar"))
print(tulisan3.replace("Surakarta", "Boyolali"))
print("=========================")

