import tkinter as tk

def hitung_total():
    harga_barang = float(entry_harga_barang.get())
    jumlah_barang = int(entry_jumlah_barang.get())
    total = harga_barang * jumlah_barang
    label_total.config(text=f"Total: Rp {total:.2f}")

# Membuat jendela utama
root = tk.Tk()
root.title("Program Kasir")

# Label dan input field untuk harga barang
label_harga_barang = tk.Label(root, text="Harga Barang (Rp):")
label_harga_barang.pack()
entry_harga_barang = tk.Entry(root)
entry_harga_barang.pack()

# Label dan input field untuk jumlah barang
label_jumlah_barang = tk.Label(root, text="Jumlah Barang:")
label_jumlah_barang.pack()
entry_jumlah_barang = tk.Entry(root)
entry_jumlah_barang.pack()

# Tombol untuk menghitung total
hitung_button = tk.Button(root, text="Hitung Total", command=hitung_total)
hitung_button.pack()

# Label untuk menampilkan total
label_total = tk.Label(root, text="")
label_total.pack()

root.mainloop()
