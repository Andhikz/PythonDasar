sisi = float(input("Masukan panjang sisi persegi: "))

keliling_persegi = 4 * sisi
luas_persegi = sisi * sisi

print(f"Keliling persegi:  {keliling_persegi}")
print(f"Luas persegi: {luas_persegi}")

panjang = float(input("Masukan panjang persegi panjang: "))
lebar = float(input("Masukan lebar persegi panjang: "))

keliling_persegi_panjang = 2 * (panjang + lebar)
luas_persegi_panjang = panjang * lebar

print(f"Keliling persegi panjang: {keliling_persegi_panjang}")
print(f"Luas persegi panjang: {luas_persegi_panjang}")

sisi_a = float(input("Masukan panjang sisi a trapesium: "))
sisi_b = float(input("Masukan panjang sisi b trapesium: "))
tinggi = float(input("Masukan tinggii trapesium: "))
sisi_miring = float(input("Masukan sisi miring trapesium: "))

keliling_trapesium = sisi_a + sisi_b + 2 * sisi_miring
luas_trapesium = 0.5 * (sisi_a + sisi_b) * tinggi 

print(f"Keliling trapesium: {keliling_trapesium}")
print(f"Luas trapesium: {luas_trapesium}")