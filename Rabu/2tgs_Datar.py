import turtle

# Buat objek Turtle
t = turtle.Turtle()

# Atur warna garis
t.pensize(2)

# Fungsi untuk menggambar bangun datar dengan warna tertentu
def gambar_bangun_datar(panjang, lebar, warna):
    t.fillcolor(warna)
    t.begin_fill()
    for _ in range(2):
        t.forward(panjang)
        t.left(90)
        t.forward(lebar)
        t.left(90)
    t.end_fill()

# Gambar Persegi Panjang dengan warna merah
t.penup()
t.goto(-150, 0)
t.pendown()
gambar_bangun_datar(100, 50, "red")

# Gambar Segitiga dengan warna kuning
t.penup()
t.goto(-20, 0)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
for _ in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()

# Gambar Trapezium dengan warna hijau
t.penup()
t.goto(110, 0)
t.pendown()
gambar_bangun_datar(80, 120, "green")

# Gambar Jajar Genjang dengan warna biru
t.penup()
t.goto(-100, -100)
t.pendown()
gambar_bangun_datar(100, 60, "blue")

# Gambar Segi Lima dengan warna ungu
t.penup()
t.goto(30, -100)
t.pendown()
t.fillcolor("purple")
t.begin_fill()
for _ in range(5):
    t.forward(80)
    t.left(72)
t.end_fill()

# Tutup jendela gambar setelah menggambar selesai
turtle.done()
