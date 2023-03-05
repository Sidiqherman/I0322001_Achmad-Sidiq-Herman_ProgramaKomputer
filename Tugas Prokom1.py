x = str(input("Nama : "))
y = int(input("Golongan : "))
z = int(input("Kelompok Jam Kerja : "))


print("=============================")
print()
gaji_pokok = y * 1000000
gaji_lembur = z * 200000
pendapatan = gaji_pokok + gaji_lembur

print("Nama : ", x)
print("Golongan : ", y)
print("Gaji pokok : ", gaji_pokok)
print("Gaji lembur : ", gaji_lembur)
print("pendapatan ", pendapatan)
print() 
