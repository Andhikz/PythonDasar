tinggi = 10  # Ubah tinggi sesuai kebutuhan

for i in range(1, tinggi + 1):
    for j in range(tinggi - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()
