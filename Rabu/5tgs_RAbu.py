import turtle

# Inisialisasi turtle
t = turtle.Turtle()
t.speed(0)  # Kecepatan maksimum

# Mengatur warna bola
t.penup()
t.color("red")
t.begin_fill()

# Menggambar lingkaran untuk bola
t.goto(0, -100)  # Pindah ke posisi tengah bola
t.pendown()
t.circle(100)  # Radius bola

# Mengakhiri pengisian warna
t.end_fill()

# Menutup jendela ketika selesai
turtle.done()