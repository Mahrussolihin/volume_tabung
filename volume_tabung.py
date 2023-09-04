print("Menghitung Volume Tabung")
print("========================")

print("Nama = Mahrus Solihin")
print("NIM = 230441100032")
print()

#coding untuk mengetahui tipe datanya
nama = "Mahrus Solihin"
print(nama, "Tipenya", type(nama))
NIM = 230441100032
print(NIM, "Tipenya", type(NIM))
print()

#coding untuk mengetahui tipe datanya
diketahui = "Diketahui"
print(diketahui, "Tipenya", type(diketahui))
phi = 3.14
print(phi, "Tipenya", type(phi))
jari_jari_tabung = 14
print(jari_jari_tabung, "Tipenya", type(jari_jari_tabung))
tinggi_tabung = 26
print(tinggi_tabung, "Tipenya", type(tinggi_tabung))
print()

print("Diketahui")
print("phi = 3.14")
print("Jari - jari tabung = 14 cm")
print("Tinggi tabung = 26 cm")
print()

#Rumus volume tabung
print("Rumus volume tabung v = phi*r*r*t")
print("Maka, phi*r*r*t = 3.14*14*14*26")

phi = 3.14
r = 14
t = 26
volume = phi*r*r*t

print()
print("----------Hasilnya----------------")
print("Volume Tabung Adalah = ", format(volume),"cm")
print()
print()
#coding 1 selesai

#coding 2
print("Volume Tabung")
print("=============")

Nama = "Mahrus Solihin"
print(Nama, "Tipe", type(Nama))
NIM = 230441100032
print(NIM, "Tipe", type(NIM))
print()

print("Diketahui")
print("phi = 3.14")
print("Jari - jari tabung = 14 cm")
print("Tinggi tabung = 26 cm")
print()

#Rumus volume tabung
print("Rumus volume tabung v = phi*r*r*t")
print("Maka, phi*r*r*t = 3.14*14*14*26")

phi = 3.14
r = 14
t = 26
volume = phi*r*r*t

def volume(phi,r,t):
    hasil = phi*r*r*t
    return hasil
print("Volume tabung adalah =", volume(phi,r,t,),"cm")
print()
print()
#coding 2 selesai

#coding 3
print("Menghitung Volume Tabung")
print("========================")

nama = "Mahrus Solihin"
print(nama, "Tipenya", type(nama))
NIM = 230441100032
print(NIM, "Tipenya", type(NIM))
print()

phi = float(input("Masukkan phi = "))
r = int(input("Masukkan jari - jari = "))
t = int(input("Masukkan tinggi = "))

def volume(phi,r,t):
    hasil = phi*r*r*t
    return hasil
print("Volume tabung adalah =", volume(phi,r,t,))
#coding 3 selesai