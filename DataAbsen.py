import os
import random
import string

data = dict()

while True:
    os.system("cls")

    print(f"{'DATA ABSEN KARYAWAN':^45}")

    keyFinal = "".join(random.choice(string.ascii_uppercase) for i in range(3))

    nama = input("Enter nama karyawan\t:")
    tanggal = input("Enter tanggal\t\t:")
    status = input("Enter status hadir\t:")

    data[keyFinal] = {'nama': nama, 'tanggal': tanggal, 'status': status}

    opsi = input("Input data lagi (y/t): ").lower()
    if opsi == 't':
        break

print("-" * 40)
print(f"Key\t Nama\t\t Tanggal\t Status")
print("-" * 40)
for key, value in data.items():
    nama = value['nama']
    tanggal = value['tanggal']
    status = value['status']
    print(f"{key}\t {nama}\t {tanggal}\t {status}")
